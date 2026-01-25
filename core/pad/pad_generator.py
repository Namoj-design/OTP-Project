# core/pad/pad_generator.py

import uuid
from core.entropy.utils import bits_to_bytes
from core.pad.pad_hash import hash_pad
from core.pad.pad_store import store_pad
from core.pad.pad_registry import register_pad


def create_pad_from_bits(bits, owner="local-user"):
    pad_bytes = bits_to_bytes(bits)
    pad_id = str(uuid.uuid4())

    pad_hash = hash_pad(pad_bytes)
    store_pad(pad_bytes, pad_id)
    register_pad(pad_id, pad_hash, owner)

    return pad_id, pad_hash