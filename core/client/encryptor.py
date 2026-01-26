# core/client/encryptor.py
from core.crypto.otp import xor_bytes
from core.pad.pad_store import load_pad
from core.pad.pad_registry import get_pad_metadata

def encrypt_message(pad_id: str, plaintext: bytes) -> bytes:
    meta = get_pad_metadata(pad_id)
    pad = load_pad(pad_id)

    offset = meta["offset_out"]
    length = len(plaintext)

    if offset + length > meta["size"]:
        raise ValueError("Pad exhausted")

    key_slice = pad[offset:offset+length]
    ciphertext = xor_bytes(plaintext, key_slice)

    meta["offset_out"] += length
    return ciphertext