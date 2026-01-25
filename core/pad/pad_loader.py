# core/pad/pad_loader.py

from core.pad.pad_store import load_pad
from core.pad.pad_hash import hash_pad
from core.pad.pad_registry import get_pad_metadata


def load_and_verify_pad(pad_id: str) -> bytes:
    pad_bytes = load_pad(pad_id)
    actual_hash = hash_pad(pad_bytes)

    meta = get_pad_metadata(pad_id)
    expected_hash = meta["hash"]

    if actual_hash != expected_hash:
        raise ValueError("Pad integrity verification failed")

    if meta["used"]:
        raise ValueError("Pad has already been marked as used")

    return pad_bytes