# tests/test_otp.py

from core.crypto.otp import encrypt, decrypt


def test_encrypt_decrypt_roundtrip():
    pad = b"\x01\x02\x03\x04"
    plaintext = b"\x10\x20\x30\x40"

    ciphertext = encrypt(plaintext, pad)
    recovered = decrypt(ciphertext, pad)

    assert recovered == plaintext


def test_xor_symmetry():
    a = b"\xAA\xBB\xCC"
    b = b"\x11\x22\x33"

    c = encrypt(a, b)
    d = encrypt(c, b)

    assert d == a