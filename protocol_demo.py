# protocol_demo.py

from core.crypto.otp import encrypt, decrypt
from core.crypto.pad_state import PadState

from core.protocol.message import MessagePacket
from core.protocol.serializer import serialize
from core.protocol.deserializer import deserialize
from core.protocol.validator import validate_packet


def main():
    print("=== Phase 5 — Message Protocol Demo ===")

    pad = b"THIS_IS_A_SECRET_PAD_1234567890"
    alice_state = PadState(pad)
    bob_state = PadState(pad)

    plaintext = b"HELLO PROTOCOL"

    pad_segment = alice_state.consume_out(len(plaintext))
    ciphertext = encrypt(plaintext, pad_segment)

    packet = MessagePacket(
        pad_id="demo-pad-001",
        offset=0,
        length=len(ciphertext),
        ciphertext=ciphertext
    )

    raw = serialize(packet)
    received = deserialize(raw)

    validate_packet(received)

    recv_segment = bob_state.consume_in(received.length)
    recovered = decrypt(received.ciphertext, recv_segment)

    print(f"Recovered: {recovered}")
    assert recovered == plaintext

    print("✓ Message packet serialized correctly")
    print("✓ Message packet validated correctly")
    print("✓ End-to-end OTP message flow works")


if __name__ == "__main__":
    main()