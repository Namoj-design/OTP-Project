from core.crypto.otp import decrypt
from core.protocol.message import MessagePacket


class Decryptor:
    def __init__(self, pad_manager):
        self.manager = pad_manager

    def decrypt_packet(self, packet: MessagePacket) -> bytes:
        # Validate pad_id
        if packet.pad_id != self.manager.pad_id:
            raise ValueError("Pad ID mismatch")

        # Validate offset (Replay protection / Ordering)
        # We must check this BEFORE consuming to prevent state corruption on bad packets
        expected_offset = self.manager.state.offset_in
        if packet.offset != expected_offset:
            raise ValueError(f"Offset mismatch! Expected {expected_offset}, got {packet.offset}")

        # Consume pad bytes (raises PadExhausted if not enough)
        pad_segment = self.manager.state.consume_in(packet.length)

        # Decrypt
        plaintext = decrypt(packet.ciphertext, pad_segment)

        # Persist state
        self.manager.persist()

        return plaintext