# core/pad/pad_registry.py

import json
import os
from datetime import datetime


REGISTRY_PATH = "data/pads/registry.json"


def _load_registry():
    if not os.path.exists(REGISTRY_PATH):
        return {}

    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)


def _save_registry(registry):
    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)

    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)


def register_pad(pad_id: str, pad_hash: str, owner: str):
    registry = _load_registry()

    registry[pad_id] = {
        "hash": pad_hash,
        "owner": owner,
        "created_at": datetime.utcnow().isoformat(),
        "used": False
    }

    _save_registry(registry)


def mark_used(pad_id: str):
    registry = _load_registry()

    if pad_id not in registry:
        raise KeyError("Pad not registered")

    registry[pad_id]["used"] = True
    _save_registry(registry)


def get_pad_metadata(pad_id: str):
    registry = _load_registry()

    if pad_id not in registry:
        raise KeyError("Pad not registered")

    return registry[pad_id]