# core/crypto/exceptions.py

class PadExhausted(Exception):
    """Raised when pad does not have enough unused material."""
    pass


class PadReuseError(Exception):
    """Raised when a compromised or reused pad is detected."""
    pass