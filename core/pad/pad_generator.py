# core/pad/pad_generator.py

from core.entropy.utils import bits_to_bytes


def create_pad_from_bits(bits) -> bytes:
    pad_bytes = bits_to_bytes(bits)
    return pad_bytes