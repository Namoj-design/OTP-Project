# core/crypto/otp.py

def xor_bytes(a: bytes, b: bytes) -> bytes:
    if len(a) != len(b):
        raise ValueError("XOR operands must be of equal length")

    return bytes(x ^ y for x, y in zip(a, b))


def encrypt(plaintext: bytes, pad_segment: bytes) -> bytes:
    """
    c = m ⊕ pad
    """
    return xor_bytes(plaintext, pad_segment)


def decrypt(ciphertext: bytes, pad_segment: bytes) -> bytes:
    """
    m = c ⊕ pad
    """
    return xor_bytes(ciphertext, pad_segment)