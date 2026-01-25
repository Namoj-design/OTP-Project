# core/crypto/pad_state.py

from core.crypto.exceptions import PadExhausted, PadReuseError


class PadState:
    """
    Enforces one-time use of pad bytes.
    Tracks offsets for outgoing and incoming directions.
    """

    def __init__(self, pad: bytes):
        self.pad = pad
        self.total_len = len(pad)

        self.offset_out = 0
        self.offset_in = 0

        self.compromised = False

    def _check_safe(self):
        if self.compromised:
            raise PadReuseError("Pad is compromised and cannot be used")

    def remaining_out(self) -> int:
        return self.total_len - self.offset_out

    def remaining_in(self) -> int:
        return self.total_len - self.offset_in

    def consume_out(self, length: int) -> bytes:
        """
        Allocate pad bytes for encryption.
        """
        self._check_safe()

        if length <= 0:
            raise ValueError("Length must be positive")

        if self.offset_out + length > self.total_len:
            self.compromised = True
            raise PadExhausted("Not enough pad material for encryption")

        start = self.offset_out
        end = start + length

        segment = self.pad[start:end]
        self.offset_out = end

        return segment

    def consume_in(self, length: int) -> bytes:
        """
        Allocate pad bytes for decryption.
        """
        self._check_safe()

        if length <= 0:
            raise ValueError("Length must be positive")

        if self.offset_in + length > self.total_len:
            self.compromised = True
            raise PadExhausted("Not enough pad material for decryption")

        start = self.offset_in
        end = start + length

        segment = self.pad[start:end]
        self.offset_in = end

        return segment