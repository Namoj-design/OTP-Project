# core/client/encryptor.py

from core.crypto.otp import encrypt
from core.protocol.message import MessagePacket


class Encryptor:
    def __init__(self, pad_manager):
        self.pad_manager = pad_manager

    def encrypt_message(self, plaintext: bytes) -> MessagePacket:
        state = self.pad_manager.state

        offset = state.offset_out
        pad_segment = state.consume_out(len(plaintext))
        ciphertext = encrypt(plaintext, pad_segment)

        packet = MessagePacket(
            pad_id=self.pad_manager.pad_id,
            offset=offset,
            length=len(ciphertext),
            ciphertext=ciphertext
        )

        self.pad_manager.persist()
        return packet