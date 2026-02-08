# core/api/exchange_api.py
import os
from core.exchange.qr_encode import pad_to_qr_frames
from core.exchange.qr_decode import import_pad_from_qr_frames

from core.pad.pad_store import load_pad

def export_pad_to_qr(pad_id: str, output_dir: str):
    pad_bytes = load_pad(pad_id)
    frames_dir, frame_count = pad_to_qr_frames(pad_bytes, output_dir=output_dir)

    return {
        "frames_dir": frames_dir,
        "frame_count": frame_count,
    }


def import_pad_from_qr(frames_dir: str, expected_hash: str | None = None):
    pad_id, pad_hash = import_pad_from_qr_frames(frames_dir, expected_hash)

    return {
        "pad_id": pad_id,
        "pad_hash": pad_hash,
    }