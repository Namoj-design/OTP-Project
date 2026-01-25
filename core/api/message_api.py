# core/api/message_api.py

from core.client.pad_manager import PadManager
from core.client.encryptor import Encryptor
from core.client.decryptor import Decryptor


def encrypt_message(pad_id: str, pad_bytes: bytes, plaintext: bytes):
    manager = PadManager(pad_id, pad_bytes)
    encryptor = Encryptor(manager)

    packet = encryptor.encrypt_message(plaintext)
    return packet


def decrypt_message(pad_id: str, pad_bytes: bytes, packet):
    manager = PadManager(pad_id, pad_bytes)
    decryptor = Decryptor(manager)

    plaintext = decryptor.decrypt_packet(packet)
    return plaintext