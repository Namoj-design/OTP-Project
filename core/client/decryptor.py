# core/client/decryptor.py

from core.crypto.otp import decrypt


class Decryptor:
    def __init__(self, pad_manager):
        self.pad_manager = pad_manager

    def decrypt_packet(self, packet):
        state = self.pad_manager.state

        if packet.offset != state.offset_in:
            raise ValueError("Offset mismatch — possible replay or loss")

        pad_segment = state.consume_in(packet.length)
        plaintext = decrypt(packet.ciphertext, pad_segment)

        self.pad_manager.persist()
        return plaintext