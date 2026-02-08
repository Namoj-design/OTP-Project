import glob
import os
import base64
from PIL import Image
from pyzbar.pyzbar import decode 

from core.exchange.markers import parse_frame
from core.pad.pad_store import save_pad
from core.pad.pad_hash import hash_pad
from core.pad.pad_registry import register_pad


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


def import_pad_from_qr_frames(frames_dir: str, expected_hash: str | None = None) -> tuple[str, str]:
    image_paths = sorted(glob.glob(os.path.join(frames_dir, "*.png")))
    if not image_paths:
        raise ValueError(f"No PNG frames found in {frames_dir}")

    total_frames = None
    chunks = {}

    for path in image_paths:
        idx, total, payload = decode_qr_frame(path)

        if total_frames is None:
            total_frames = total
        elif total != total_frames:
            raise ValueError(f"Frame total mismatch in {path}: expected {total_frames}, got {total}")

        if idx in chunks:
            # Duplicate frame is fine, just ignore or overwrite
            pass
        
        chunks[idx] = payload

    # Verify we have all frames
    if len(chunks) != total_frames:
        missing = set(range(total_frames)) - set(chunks.keys())
        raise ValueError(f"Missing frames: {missing}")

    # Reassemble bytes
    pad_bytes = bytearray()
    for i in range(total_frames):
        pad_bytes.extend(chunks[i])
    
    pad_bytes = bytes(pad_bytes)

    # Verify hash if provided
    actual_hash = hash_pad(pad_bytes)
    if expected_hash and actual_hash != expected_hash:
        raise ValueError(f"Hash mismatch! Expected {expected_hash}, got {actual_hash}")

    # Save and register
    pad_id = save_pad(pad_bytes)
    register_pad(pad_id, actual_hash, "imported-pad", len(pad_bytes))

    return pad_id, actual_hash