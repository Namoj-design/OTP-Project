# api_demo.py

from core.api.pad_api import generate_pad_from_image, load_pad
from core.api.message_api import encrypt_message, decrypt_message
from core.api.exchange_api import export_pad_to_qr, import_pad_from_qr


def main():
    print("=== Phase 7 — API Layer Demo ===")

    # Generate pad
    pad_id, pad_hash = generate_pad_from_image(
        "data/sample_images/test.jpg",
        owner="alice"
    )

    pad_bytes = load_pad(pad_id)

    print(f"Pad ID:   {pad_id}")
    print(f"Pad hash: {pad_hash}")
    print(f"Pad size: {len(pad_bytes)} bytes")

    # QR exchange
    frames = export_pad_to_qr(pad_bytes)
    reconstructed = import_pad_from_qr(frames, pad_hash)

    assert reconstructed == pad_bytes
    print("✓ QR exchange via API works")

    # Message encryption
    plaintext = b"HELLO API LAYER"
    packet = encrypt_message(pad_id, pad_bytes, plaintext)

    recovered = decrypt_message(pad_id, pad_bytes, packet)

    print(f"Recovered: {recovered}")
    assert recovered == plaintext

    print("✓ API encryption/decryption works")
    print("✓ Full OTP pipeline accessible via API")


if __name__ == "__main__":
    main()