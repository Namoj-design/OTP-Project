# core/exchange/qr_encode.py

import base64
import os
import qrcode

from core.exchange.chunking import chunk_bytes
from core.exchange.markers import make_frame


QR_DIR = "data/qr_frames"


def pad_to_qr_frames(pad_bytes: bytes, chunk_size: int = 800):
    os.makedirs(QR_DIR, exist_ok=True)

    chunks = chunk_bytes(pad_bytes, chunk_size)
    total = len(chunks)

    frame_paths = []

    for i, chunk in enumerate(chunks):
        frame = make_frame(i, total, chunk)
        b64 = base64.b64encode(frame).decode()

        img = qrcode.make(b64)
        path = os.path.join(QR_DIR, f"frame_{i:04d}.png")
        img.save(path)

        frame_paths.append(path)

    return frame_paths