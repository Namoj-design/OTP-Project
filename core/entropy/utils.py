# core/entropy/utils.py

def bits_to_bytes(bits):
    """
    Convert a list of bits into bytes.
    """
    out = bytearray()

    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(bits):
                byte = (byte << 1) | bits[i + j]
        out.append(byte)

    return bytes(out)