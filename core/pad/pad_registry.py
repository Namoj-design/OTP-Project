# core/pad/pad_registry.py

PAD_REGISTRY = {}


def register_pad(pad_id: str, pad_hash: str, owner: str, size: int):
    PAD_REGISTRY[pad_id] = {
        "pad_hash": pad_hash,
        "owner": owner,
        "size": size,
        "offset_out": 0,
        "offset_in": 0,
    }


def get_pad_metadata(pad_id: str):
    if pad_id not in PAD_REGISTRY:
        raise KeyError("Pad not registered")

    return PAD_REGISTRY[pad_id]


def update_offsets(pad_id: str, offset_out: int = None, offset_in: int = None):
    if pad_id not in PAD_REGISTRY:
        raise KeyError("Pad not registered")

    meta = PAD_REGISTRY[pad_id]

    if offset_out is not None:
        meta["offset_out"] = offset_out

    if offset_in is not None:
        meta["offset_in"] = offset_in