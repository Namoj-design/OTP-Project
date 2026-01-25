# core/exchange/verifier.py

from core.pad.pad_hash import hash_pad


def reassemble_and_verify(frames, expected_hash: str):
    """
    frames: list of (index, total, payload)
    """
    frames_sorted = sorted(frames, key=lambda x: x[0])

    total = frames_sorted[0][1]
    if len(frames_sorted) != total:
        raise ValueError("Missing QR frames")

    pad_bytes = b"".join(payload for _, _, payload in frames_sorted)
    actual_hash = hash_pad(pad_bytes)

    if actual_hash != expected_hash:
        raise ValueError("Pad hash mismatch after QR exchange")

    return pad_bytes