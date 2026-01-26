import os
import uuid

PAD_DIR = os.path.join(os.path.dirname(__file__), "pads")
os.makedirs(PAD_DIR, exist_ok=True)


def load_pad(pad_id: str) -> bytes:
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")
    with open(path, "rb") as f:
        return f.read()


def save_pad(pad_bytes: bytes) -> str:
    if not isinstance(pad_bytes, (bytes, bytearray)):
        raise TypeError(f"save_pad expected bytes, got {type(pad_bytes)}")

    pad_id = str(uuid.uuid4())
    path = os.path.join(PAD_DIR, f"{pad_id}.bin")

    with open(path, "wb") as f:
        f.write(pad_bytes)

    return pad_id


def store_pad(pad_bytes: bytes, pad_id: str | None = None) -> str:
    if not isinstance(pad_bytes, (bytes, bytearray)):
        raise TypeError(f"store_pad expected bytes, got {type(pad_bytes)}")

    # Old code path: caller provides pad_id
    if pad_id is not None:
        path = os.path.join(PAD_DIR, f"{pad_id}.bin")
        with open(path, "wb") as f:
            f.write(pad_bytes)
        return pad_id

    # New code path: generate a fresh ID
    return save_pad(pad_bytes)