# core/entropy/randomness_tests.py

import math


def frequency_test(bits):
    """
    Test balance of 0s and 1s.
    """
    n = len(bits)
    ones = sum(bits)
    zeros = n - ones

    if n == 0:
        return False, 0.0

    imbalance = abs(ones - zeros) / n
    return imbalance < 0.05, imbalance


def chi_square_test(bits):
    """
    Pearson chi-square test for 0/1 distribution.
    """
    n = len(bits)
    ones = sum(bits)
    zeros = n - ones

    if n == 0:
        return False, 0.0

    expected = n / 2
    chi2 = ((zeros - expected) ** 2) / expected + ((ones - expected) ** 2) / expected

    return chi2 < 3.84, chi2  # 95% confidence