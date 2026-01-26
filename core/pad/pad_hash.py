# core/pad/pad_hash.py
import hashlib

def hash_pad(pad_bytes: bytes) -> str:
    if not isinstance(pad_bytes, (bytes, bytearray)):
        raise TypeError("pad_bytes must be bytes")

    return hashlib.sha256(pad_bytes).hexdigest()