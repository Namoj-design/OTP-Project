# core/exchange/qr_encode.py

import base64
import os
import qrcode

from core.exchange.chunking import chunk_bytes
from core.exchange.markers import make_frame


def pad_to_qr_frames(pad_bytes: bytes, output_dir: str = "data/qr_frames", chunk_size: int = 800) -> tuple[str, int]:
    os.makedirs(output_dir, exist_ok=True)

    chunks = chunk_bytes(pad_bytes, chunk_size)
    total = len(chunks)

    frame_paths = []

    for i, chunk in enumerate(chunks):
        # Enforce bytes invariant for QR payload
        if isinstance(chunk, str):
            chunk = chunk.encode()

        frame = make_frame(i, total, chunk)
        b64 = base64.b64encode(frame).decode("ascii")

        img = qrcode.make(b64)
        path = os.path.join(output_dir, f"frame_{i:04d}.png")
        img.save(path)

        frame_paths.append(path)

    return output_dir, len(frame_paths)