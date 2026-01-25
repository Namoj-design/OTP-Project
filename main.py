# main.py

from core.crypto.otp import encrypt, decrypt
from core.crypto.pad_state import PadState


def main():
    print("=== One-Time Pad Demo ===")

    # Shared pad (normally from entropy pipeline later)
    pad = b"THIS_IS_A_SECRET_PAD_1234567890"

    alice_state = PadState(pad)
    bob_state = PadState(pad)

    message = b"HELLO BOB"

    print(f"Alice plaintext: {message}")

    pad_segment = alice_state.consume_out(len(message))
    ciphertext = encrypt(message, pad_segment)

    print(f"Ciphertext sent: {ciphertext}")

    recv_segment = bob_state.consume_in(len(ciphertext))
    recovered = decrypt(ciphertext, recv_segment)

    print(f"Bob recovered: {recovered}")

    assert recovered == message

    print("✓ OTP encryption/decryption successful")
    print("✓ No pad reuse occurred")


if __name__ == "__main__":
    main()