# core/api/exchange_api.py

import os

from core.exchange.qr_encode import pad_to_qr_frames
from core.exchange.qr_decode import decode_qr_frame
from core.exchange.verifier import reassemble_and_verify
from core.pad.pad_loader import load_pad


def export_pad_to_qr(pad_id: str):
    # Load pad bytes by ID
    pad_bytes = load_pad(pad_id)

    # Generate QR frame image files
    frame_paths = pad_to_qr_frames(pad_bytes)

    # Derive output directory and frame count
    output_dir = os.path.dirname(frame_paths[0]) if frame_paths else None
    frame_count = len(frame_paths)

    return output_dir, frame_count


def import_pad_from_qr(frame_paths, expected_hash: str):
    frames = []

    for path in frame_paths:
        frames.append(decode_qr_frame(path))

    return reassemble_and_verify(frames, expected_hash)