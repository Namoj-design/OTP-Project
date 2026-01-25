# core/pad/pad_store.py

import os


PAD_DIR = "data/pads"


def store_pad(pad_bytes: bytes, pad_id: str):
    """
    Store pad bytes locally under pad_id.bin.
    """
    os.makedirs(PAD_DIR, exist_ok=True)

    path = os.path.join(PAD_DIR, f"{pad_id}.bin")

    with open(path, "wb") as f:
        f.write(pad_bytes)

    return path


def load_pad(pad_id: str) -> bytes:
    """
    Load pad bytes by pad_id.
    """
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Pad not found: {pad_id}")

    with open(path, "rb") as f:
        return f.read()