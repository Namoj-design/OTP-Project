# core/api/pad_api.py
import os
from core.entropy.camera import load_image_pixels
from core.entropy.rgb_collapse import pixels_to_bits
from core.entropy.thinning import thin_bits
from core.entropy.von_neumann import von_neumann_extract

from core.pad.pad_generator import create_pad_from_bits
from core.pad.pad_store import save_pad, load_pad
from core.pad.pad_hash import hash_pad
from core.pad.pad_registry import register_pad, get_pad_metadata

def generate_pad_from_image(image_path: str, owner="local-user"):
    if not os.path.exists(image_path):
        raise ValueError("Entropy image not found")

    pixels = load_image_pixels(image_path)
    bits = pixels_to_bits(pixels)
    bits = thin_bits(bits, k=3)
    bits = von_neumann_extract(bits)

    pad_bytes = create_pad_from_bits(bits, owner)

    pad_id = save_pad(pad_bytes)
    pad_hash = hash_pad(pad_bytes)

    register_pad(
        pad_id=pad_id,
        pad_hash=pad_hash,
        owner=owner,
        size=len(pad_bytes),
    )

    return {
        "pad_id": pad_id,
        "pad_size": len(pad_bytes),
        "pad_hash": pad_hash,
    }


def pad_status(pad_id: str):
    meta = get_pad_metadata(pad_id)

    remaining = meta["size"] - meta["offset_out"]

    return {
        "pad_id": pad_id,
        "pad_size": meta["size"],
        "pad_hash": meta["pad_hash"],
        "offset_out": meta["offset_out"],
        "offset_in": meta["offset_in"],
        "remaining": remaining,
    }