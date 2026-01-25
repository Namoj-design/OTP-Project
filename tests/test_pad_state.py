# tests/test_pad_state.py

import pytest
from core.crypto.pad_state import PadState
from core.crypto.exceptions import PadExhausted, PadReuseError


def test_basic_consumption():
    pad = b"ABCDEFGH"
    state = PadState(pad)

    seg1 = state.consume_out(3)
    seg2 = state.consume_out(2)

    assert seg1 == b"ABC"
    assert seg2 == b"DE"
    assert state.offset_out == 5


def test_exhaustion():
    pad = b"ABCDE"
    state = PadState(pad)

    state.consume_out(5)

    with pytest.raises(PadExhausted):
        state.consume_out(1)


def test_compromised_after_exhaustion():
    pad = b"ABCDE"
    state = PadState(pad)

    try:
        state.consume_out(6)
    except PadExhausted:
        pass

    with pytest.raises(PadReuseError):
        state.consume_out(1)


def test_in_and_out_independent():
    pad = b"ABCDEFGH"
    state = PadState(pad)

    out_seg = state.consume_out(3)
    in_seg = state.consume_in(3)

    assert out_seg == b"ABC"
    assert in_seg == b"ABC"
    assert state.offset_out == 3
    assert state.offset_in == 3