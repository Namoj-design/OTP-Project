# core/protocol/message.py

from dataclasses import dataclass


@dataclass
class MessagePacket:
    pad_id: str
    offset: int
    length: int
    ciphertext: bytes