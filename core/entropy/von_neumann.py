# core/entropy/von_neumann.py

def von_neumann_extract(bits):
    """
    Apply von Neumann extractor to remove bias.
    """
    extracted = []

    i = 0
    while i + 1 < len(bits):
        a = bits[i]
        b = bits[i + 1]

        if a == 0 and b == 1:
            extracted.append(0)
        elif a == 1 and b == 0:
            extracted.append(1)

        i += 2

    return extracted