# backend_demo.py

import requests

from core.api.pad_api import generate_pad_from_image, load_pad
from core.api.message_api import encrypt_message, decrypt_message


def main():
    print("=== Phase 8 — Backend Mailbox Demo ===")

    # Generate pad
    pad_id, pad_hash = generate_pad_from_image(
        "data/sample_images/test.jpg",
        owner="alice"
    )

    pad_bytes = load_pad(pad_id)

    # Alice encrypts message
    plaintext = b"HELLO THROUGH SERVER"
    packet = encrypt_message(pad_id, pad_bytes, plaintext)

    # Send to server
    res = requests.post(
        "http://127.0.0.1:8000/send",
        json={
            "pad_id": pad_id,
            "sender": "alice",
            "recipient": "bob",
            "packet": packet.ciphertext.hex()
        }
    )

    assert res.status_code == 200
    print("✓ Message stored on server")

    # Bob fetches
    res = requests.get("http://127.0.0.1:8000/fetch/bob")
    data = res.json()

    msg = data["messages"][0]
    ciphertext = bytes.fromhex(msg["packet"])

    # Reconstruct packet
    from core.protocol.message import MessagePacket
    packet_obj = MessagePacket(
        pad_id=msg["pad_id"],
        offset=0,
        length=len(ciphertext),
        ciphertext=ciphertext
    )

    recovered = decrypt_message(pad_id, pad_bytes, packet_obj)

    print(f"Recovered: {recovered}")
    assert recovered == plaintext

    print("✓ End-to-end OTP via server works")
    print("✓ Server never saw plaintext or keys")


if __name__ == "__main__":
    main()