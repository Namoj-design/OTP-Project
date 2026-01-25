# core/protocol/deserializer.py

from core.protocol.message import MessagePacket


def deserialize(data: bytes) -> MessagePacket:
    i = 0

    pad_id_len = int.from_bytes(data[i:i+2], "big")
    i += 2

    pad_id = data[i:i+pad_id_len].decode()
    i += pad_id_len

    offset = int.from_bytes(data[i:i+8], "big")
    i += 8

    length = int.from_bytes(data[i:i+4], "big")
    i += 4

    ciphertext = data[i:i+length]

    return MessagePacket(
        pad_id=pad_id,
        offset=offset,
        length=length,
        ciphertext=ciphertext
    )