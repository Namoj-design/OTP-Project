# pad_demo.py

from core.entropy.camera import load_image_pixels
from core.entropy.rgb_collapse import pixels_to_bits
from core.entropy.thinning import thin_bits
from core.entropy.von_neumann import von_neumann_extract
from core.pad.pad_generator import create_pad_from_bits
from core.pad.pad_loader import load_and_verify_pad


def main():
    print("=== Phase 3 — Pad Lifecycle Demo ===")

    pixels = load_image_pixels("data/sample_images/test.jpg")
    bits = pixels_to_bits(pixels)
    bits = thin_bits(bits, k=3)
    bits = von_neumann_extract(bits)

    pad_id, pad_hash = create_pad_from_bits(bits, owner="alice")

    print(f"Pad ID:   {pad_id}")
    print(f"Pad hash: {pad_hash}")

    pad_bytes = load_and_verify_pad(pad_id)

    print(f"Loaded pad size: {len(pad_bytes)} bytes")
    print("✓ Pad integrity verified")
    print("✓ Pad lifecycle discipline working")


if __name__ == "__main__":
    main()