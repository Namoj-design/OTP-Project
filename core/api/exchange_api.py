# core/api/exchange_api.py

from core.exchange.qr_encode import pad_to_qr_frames
from core.exchange.qr_decode import decode_qr_frame
from core.exchange.verifier import reassemble_and_verify


def export_pad_to_qr(pad_bytes: bytes):
    return pad_to_qr_frames(pad_bytes)


def import_pad_from_qr(frame_paths, expected_hash: str):
    frames = []

    for path in frame_paths:
        frames.append(decode_qr_frame(path))

    return reassemble_and_verify(frames, expected_hash)