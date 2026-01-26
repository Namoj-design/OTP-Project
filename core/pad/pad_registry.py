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


def register_pad(pad_id, pad_hash, owner, size):
    registry = _load_registry()

    registry[pad_id] = {
        "pad_hash": pad_hash,
        "owner": owner,
        "size": size,
        "offset_out": 0,
        "offset_in": 0,
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