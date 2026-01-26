import hashlib

def hash_pad(pad_bytes: bytes) -> str:
    if isinstance(pad_bytes, str):
        pad_bytes = pad_bytes.encode("utf-8")

    if not isinstance(pad_bytes, (bytes, bytearray)):
        raise TypeError(f"hash_pad expected bytes, got {type(pad_bytes)}")

    h = hashlib.sha256()
    h.update(pad_bytes)
    return h.hexdigest()