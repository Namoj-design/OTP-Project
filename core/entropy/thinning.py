# core/entropy/thinning.py

def thin_bits(bits, k=3):
    """
    Keep only every k-th bit.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    return [bit for i, bit in enumerate(bits) if i % k == 0]