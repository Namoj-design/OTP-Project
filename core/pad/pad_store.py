import os
import uuid

PAD_DIR = os.path.join(os.path.dirname(__file__), "pads")

def load_pad(pad_id: str) -> bytes:
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")
    with open(path, "rb") as f:
        return f.read()

def save_pad(pad_bytes: bytes) -> str:
    os.makedirs(PAD_DIR, exist_ok=True)

    pad_id = str(uuid.uuid4())
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")

    with open(path, "wb") as f:
        f.write(pad_bytes)

    return pad_id

def store_pad(pad_bytes: bytes) -> str:
    # Backward-compat alias for older code paths
    return save_pad(pad_bytes)