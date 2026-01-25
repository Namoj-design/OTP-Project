# core/exchange/qr_decode.py

import base64
from PIL import Image
from pyzbar.pyzbar import decode  # type: ignore

from core.exchange.markers import parse_frame


def decode_qr_frame(path: str):
    """
    Decode a single QR frame image into (index, total, payload).
    """
    img = Image.open(path)
    decoded = decode(img)

    if not decoded:
        raise ValueError(f"No QR code found in {path}")

    if len(decoded) > 1:
        raise ValueError(f"Multiple QR codes found in {path}")

    data = decoded[0].data.decode()
    frame_bytes = base64.b64decode(data)

    return parse_frame(frame_bytes)