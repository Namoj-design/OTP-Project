from core.crypto.otp import encrypt
from core.protocol.message import MessagePacket


class Encryptor:
    def __init__(self, pad_manager):
        self.manager = pad_manager

    def encrypt_message(self, plaintext: bytes) -> MessagePacket:
        # Get length
        length = len(plaintext)
        
        # Current offset for packet metadata (before consumption)
        offset = self.manager.state.offset_out

        # Consume pad bytes (raises PadExhausted if not enough)
        pad_segment = self.manager.state.consume_out(length)

        # Encrypt
        ciphertext = encrypt(plaintext, pad_segment)

        # Persist state
        self.manager.persist()

        # Create packet
        packet = MessagePacket(
            pad_id=self.manager.pad_id,
            offset=offset,
            length=length,
            ciphertext=ciphertext
        )

        return packet