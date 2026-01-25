# core/entropy/rgb_collapse.py

def rgb_to_bit(rgb):
    """
    Collapse one RGB pixel into a single bit by XORing all 24 bits.
    """
    r, g, b = rgb
    value = (r << 16) | (g << 8) | b

    bit = 0
    for i in range(24):
        bit ^= (value >> i) & 1

    return bit


def pixels_to_bits(pixels):
    """
    Convert a list of RGB tuples into a list of bits.
    """
    return [rgb_to_bit(p) for p in pixels]