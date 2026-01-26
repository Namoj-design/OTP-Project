# core/pad/pad_generator.py
import os
from typing import Tuple

def create_pad_from_bits(bits: list[int], owner: str = "local-user") -> bytes:
    if not bits:
        raise ValueError("No entropy bits provided")

    # pack bits → bytes
    b = bytearray()
    cur = 0
    count = 0

    for bit in bits:
        cur = (cur << 1) | (bit & 1)
        count += 1
        if count == 8:
            b.append(cur)
            cur = 0
            count = 0

    if count > 0:
        b.append(cur << (8 - count))

    # mix OS entropy to guarantee uniqueness
    b.extend(os.urandom(64))

    return bytes(b)