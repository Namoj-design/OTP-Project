# core/pad/pad_hash.py

import hashlib


def hash_pad(pad_bytes: bytes) -> str:
    """
    Compute SHA-256 hash of pad bytes.
    Returns hex digest.
    """
    h = hashlib.sha256()
    h.update(pad_bytes)
    return h.hexdigest()