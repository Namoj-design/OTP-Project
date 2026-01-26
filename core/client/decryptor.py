# core/client/decryptor.py
from core.crypto.otp import xor_bytes
from core.pad.pad_store import load_pad
from core.pad.pad_registry import get_pad_metadata

def decrypt_message(pad_id: str, ciphertext: bytes, offset: int) -> bytes:
    meta = get_pad_metadata(pad_id)
    pad = load_pad(pad_id)

    if offset != meta["offset_in"]:
        raise ValueError("Replay or out-of-order message detected")

    length = len(ciphertext)
    key_slice = pad[offset:offset+length]

    plaintext = xor_bytes(ciphertext, key_slice)

    meta["offset_in"] += length
    return plaintext