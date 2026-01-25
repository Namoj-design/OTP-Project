# core/protocol/validator.py

def validate_packet(packet):
    if packet.length != len(packet.ciphertext):
        raise ValueError("Ciphertext length mismatch")

    if packet.offset < 0:
        raise ValueError("Negative offset")

    if packet.length <= 0:
        raise ValueError("Invalid length")