# core/client/offset_store.py

import json
import os

OFFSET_DIR = "data/offsets"


def _path(pad_id: str):
    os.makedirs(OFFSET_DIR, exist_ok=True)
    return os.path.join(OFFSET_DIR, f"{pad_id}.json")


def save_offsets(pad_id: str, offset_out: int, offset_in: int):
    path = _path(pad_id)
    tmp = path + ".tmp"

    with open(tmp, "w") as f:
        json.dump(
            {"offset_out": offset_out, "offset_in": offset_in},
            f,
            indent=2
        )

    os.replace(tmp, path)  # atomic on POSIX


def load_offsets(pad_id: str):
    path = _path(pad_id)

    if not os.path.exists(path):
        return 0, 0

    with open(path, "r") as f:
        data = json.load(f)

    return data["offset_out"], data["offset_in"]