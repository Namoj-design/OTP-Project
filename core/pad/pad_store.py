import os
import uuid

PAD_DIR = os.path.join(os.path.dirname(__file__), "pads")

def load_pad(pad_id: str) -> bytes:
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")
    with open(path, "rb") as f:
        return f.read()

def save_pad(pad_bytes) -> str:
    os.makedirs(PAD_DIR, exist_ok=True)

    # Defensive: unwrap accidental tuple (pad_bytes, pad_id)
    if isinstance(pad_bytes, tuple):
        pad_bytes = pad_bytes[0]

    # Defensive: handle accidental str instead of bytes
    if isinstance(pad_bytes, str):
        pad_bytes = pad_bytes.encode("utf-8")

    pad_id = str(uuid.uuid4())
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")

    with open(path, "wb") as f:
        f.write(pad_bytes)

    return pad_id

def store_pad(pad_bytes: bytes, pad_id: str | None = None) -> str:
    os.makedirs(PAD_DIR, exist_ok=True)

    # If caller provided an ID (old code path), honor it
    if pad_id is not None:
        path = os.path.join(PAD_DIR, f"{pad_id}.bin")

        with open(path, "wb") as f:
            f.write(pad_bytes)

        return pad_id

    # Otherwise generate a fresh ID (new code path)
    return save_pad(pad_bytes)