# entropy_demo.py

from core.entropy.camera import load_image_pixels
from core.entropy.rgb_collapse import pixels_to_bits
from core.entropy.thinning import thin_bits
from core.entropy.von_neumann import von_neumann_extract
from core.entropy.randomness_tests import frequency_test, chi_square_test
from core.entropy.utils import bits_to_bytes


def main():
    print("=== Phase 2 — Entropy → Randomness Demo ===")

    pixels = load_image_pixels("data/sample_images/test.jpg")

    bits_raw = pixels_to_bits(pixels)
    print(f"Raw bits: {len(bits_raw)}")

    bits_thin = thin_bits(bits_raw, k=3)
    print(f"After thinning: {len(bits_thin)}")

    bits_clean = von_neumann_extract(bits_thin)
    print(f"After von Neumann: {len(bits_clean)}")

    ok_freq, imbalance = frequency_test(bits_clean)
    ok_chi, chi2 = chi_square_test(bits_clean)

    print(f"Frequency test ok: {ok_freq}, imbalance={imbalance:.4f}")
    print(f"Chi-square test ok: {ok_chi}, chi2={chi2:.4f}")

    pad_bytes = bits_to_bytes(bits_clean)
    print(f"Final pad size (bytes): {len(pad_bytes)}")

    with open("data/pads/pad.bin", "wb") as f:
        f.write(pad_bytes)

    print("✓ Pad written to data/pads/pad.bin")


if __name__ == "__main__":
    main()