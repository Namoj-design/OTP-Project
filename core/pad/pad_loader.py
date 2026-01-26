# core/pad/pad_loader.py

from core.pad.pad_store import load_pad
from core.pad.pad_hash import hash_pad
from core.pad.pad_registry import get_pad_metadata


def load_and_verify_pad(pad_id: str):
    pad_bytes = load_pad(pad_id)
    meta = get_pad_metadata(pad_id)

    computed_hash = hash_pad(pad_bytes)
    expected_hash = meta["pad_hash"]

    if computed_hash != expected_hash:
        raise ValueError("Pad hash mismatch")

    size = meta["size"]
    offset_out = meta["offset_out"]
    offset_in = meta["offset_in"]

    remaining = size - max(offset_out, offset_in)

    return {
        "pad_id": pad_id,
        "pad_size": size,
        "pad_hash": expected_hash,
        "offset_out": offset_out,
        "offset_in": offset_in,
        "remaining": remaining,
    }