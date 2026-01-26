# core/api/pad_api.py

from core.pad.pad_loader import load_and_verify_pad
from core.pad.pad_generator import create_pad_from_bits
from core.entropy.camera import load_image_pixels
from core.entropy.rgb_collapse import pixels_to_bits
from core.entropy.thinning import thin_bits
from core.entropy.von_neumann import von_neumann_extract


def generate_pad_from_image(image_path: str, owner="local-user"):
    pixels = load_image_pixels(image_path)
    bits = pixels_to_bits(pixels)
    bits = thin_bits(bits, k=3)
    bits = von_neumann_extract(bits)

    # Create pad bytes from extracted bits
    pad_bytes, _ = create_pad_from_bits(bits, owner)

    # Persist pad and get pad_id
    from core.pad.pad_store import store_pad
    pad_id = store_pad(pad_bytes)

    # Compute cryptographic hash of pad bytes
    from core.pad.pad_hash import hash_pad
    pad_hash = hash_pad(pad_bytes)

    return {
        "pad_id": pad_id,
        "pad_size": len(pad_bytes),
        "pad_hash": pad_hash,
    }


def load_pad(pad_id: str):
    return load_and_verify_pad(pad_id)