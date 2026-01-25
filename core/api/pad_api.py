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

    return create_pad_from_bits(bits, owner)


def load_pad(pad_id: str):
    return load_and_verify_pad(pad_id)