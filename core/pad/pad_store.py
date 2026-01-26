# core/pad/pad_store.py
import os
import uuid

PAD_DIR = "data/pads"
os.makedirs(PAD_DIR, exist_ok=True)

def save_pad(pad_bytes: bytes) -> str:
    if not isinstance(pad_bytes, (bytes, bytearray)):
        raise TypeError("pad_bytes must be bytes")

    pad_id = str(uuid.uuid4())
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")

    with open(path, "wb") as f:
        f.write(pad_bytes)

    return pad_id


def load_pad(pad_id: str) -> bytes:
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")

    if not os.path.exists(path):
        raise FileNotFoundError("Pad not found")

    with open(path, "rb") as f:
        return f.read()