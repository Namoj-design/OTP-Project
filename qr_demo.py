# qr_demo.py

from core.entropy.camera import load_image_pixels
from core.entropy.rgb_collapse import pixels_to_bits
from core.entropy.thinning import thin_bits
from core.entropy.von_neumann import von_neumann_extract

from core.pad.pad_generator import create_pad_from_bits
from core.pad.pad_loader import load_and_verify_pad
from core.pad.pad_hash import hash_pad

from core.exchange.qr_encode import pad_to_qr_frames
from core.exchange.qr_decode import decode_qr_frame
from core.exchange.verifier import reassemble_and_verify


def main():
    print("=== Phase 4 — QR Pad Exchange Demo ===")

    # Alice side: generate pad
    pixels = load_image_pixels("data/sample_images/test.jpg")
    bits = pixels_to_bits(pixels)
    bits = thin_bits(bits, k=3)
    bits = von_neumann_extract(bits)

    pad_id, pad_hash = create_pad_from_bits(bits, owner="alice")
    pad_bytes = load_and_verify_pad(pad_id)

    print(f"Alice pad ID:   {pad_id}")
    print(f"Alice pad hash: {pad_hash}")
    print(f"Alice pad size: {len(pad_bytes)} bytes")

    # Alice side: QR encode
    frame_paths = pad_to_qr_frames(pad_bytes)
    print(f"Generated {len(frame_paths)} QR frames")

    # Bob side: QR decode (simulated by reading files)
    frames = []
    for path in frame_paths:
        index, total, payload = decode_qr_frame(path)
        frames.append((index, total, payload))

    # Bob side: verify + reassemble
    reconstructed = reassemble_and_verify(frames, pad_hash)

    print(f"Bob reconstructed pad size: {len(reconstructed)} bytes")

    assert reconstructed == pad_bytes

    print("✓ QR pad exchange successful")
    print("✓ Pad integrity preserved")
    print("✓ Air-gapped transfer discipline works")


if __name__ == "__main__":
    main()