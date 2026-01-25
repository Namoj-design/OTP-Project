# core/exchange/markers.py

def make_frame(index: int, total: int, payload: bytes) -> bytes:
    if isinstance(payload, str):
        payload = payload.encode()

    return (
        index.to_bytes(4, "big") +
        total.to_bytes(4, "big") +
        payload
    )

def parse_frame(frame: bytes):
    index = int.from_bytes(frame[0:4], "big")
    total = int.from_bytes(frame[4:8], "big")
    payload = frame[8:]
    return index, total, payload