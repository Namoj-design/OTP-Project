import json
import os
import fcntl
from typing import Dict, Any

REGISTRY_PATH = "data/registry.json"

class RegistryCorruptedException(Exception):
    pass

class PadNotFoundError(Exception):
    pass

def _load_registry() -> Dict[str, Any]:
    if not os.path.exists(REGISTRY_PATH):
        return {"pads": {}}
    
    try:
        with open(REGISTRY_PATH, "r") as f:
            fcntl.flock(f, fcntl.LOCK_SH)
            try:
                data = json.load(f)
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)
            return data
    except json.JSONDecodeError:
        raise RegistryCorruptedException("Registry JSON is corrupted")

def _save_registry(data: Dict[str, Any]):
    # atomic write pattern
    temp_path = REGISTRY_PATH + ".tmp"
    with open(temp_path, "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            json.dump(data, f, indent=2)
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)
    
    os.rename(temp_path, REGISTRY_PATH)

def register_pad(pad_id: str, pad_hash: str, owner: str, size: int):
    data = _load_registry()
    data["pads"][pad_id] = {
        "pad_id": pad_id,
        "pad_hash": pad_hash,
        "owner": owner,
        "size": size,
        "created_at": str(os.path.getctime(REGISTRY_PATH) if os.path.exists(REGISTRY_PATH) else 0),
        "offset_out": 0,
        "offset_in": 0,
    }
    _save_registry(data)

def get_pad_metadata(pad_id: str) -> Dict[str, Any]:
    data = _load_registry()
    if pad_id not in data["pads"]:
        raise PadNotFoundError(f"Pad {pad_id} not found in registry")
    return data["pads"][pad_id]

def update_offsets(pad_id: str, offset_in: int = None, offset_out: int = None):
    data = _load_registry()
    if pad_id not in data["pads"]:
        raise PadNotFoundError(f"Pad {pad_id} not registered")
    
    if offset_in is not None:
        data["pads"][pad_id]["offset_in"] = offset_in
    if offset_out is not None:
        data["pads"][pad_id]["offset_out"] = offset_out
        
    _save_registry(data)

def list_pads():
    data = _load_registry()
    return list(data["pads"].values())