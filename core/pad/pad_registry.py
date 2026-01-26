# core/pad/pad_registry.py
_registry = {}

def register_pad(pad_id: str, pad_hash: str, owner: str, size: int):
    _registry[pad_id] = {
        "pad_id": pad_id,
        "pad_hash": pad_hash,
        "owner": owner,
        "size": size,
        "offset_out": 0,
        "offset_in": 0,
    }

def get_pad_metadata(pad_id: str):
    if pad_id not in _registry:
        raise KeyError("Pad not registered")
    return _registry[pad_id]