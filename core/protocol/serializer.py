# core/protocol/serializer.py

from core.protocol.message import MessagePacket


def serialize(packet: MessagePacket) -> bytes:
    pad_id_bytes = packet.pad_id.encode()
    pad_id_len = len(pad_id_bytes)

    header = (
        pad_id_len.to_bytes(2, "big") +
        pad_id_bytes +
        packet.offset.to_bytes(8, "big") +
        packet.length.to_bytes(4, "big")
    )

    return header + packet.ciphertext