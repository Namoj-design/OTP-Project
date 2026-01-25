# core/exchange/qr_decode.py

import base64
from PIL import Image
from pyzbar.pyzbar import decode

from core.exchange.markers import parse_frame


def decode_qr_frame(path: str):
    img = Image.open(path)
    decoded = decode(img)

    if not decoded:
        raise ValueError(f"No QR code found in {path}")

    data = decoded[0].data.decode()
    frame = base64.b64decode(data)

    return parse_frame(frame)