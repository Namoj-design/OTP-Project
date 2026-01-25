# ui_api_server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.api.pad_api import generate_pad_from_image, load_pad
from core.api.message_api import encrypt_message
from core.client.offset_store import load_offsets
from core.api.exchange_api import export_pad_to_qr, import_pad_from_qr


app = FastAPI(title="OTP Local UI API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GeneratePadRequest(BaseModel):
    image_path: str


class EncryptRequest(BaseModel):
    pad_id: str
    message: str


@app.post("/generate_pad")
def generate_pad(req: GeneratePadRequest):
    pad_id, pad_hash = generate_pad_from_image(req.image_path)
    return {"pad_id": pad_id, "pad_hash": pad_hash}


@app.get("/pad_status/{pad_id}")
def pad_status(pad_id: str):
    pad_bytes = load_pad(pad_id)
    out_off, in_off = load_offsets(pad_id)

    return {
        "pad_id": pad_id,
        "pad_size": len(pad_bytes),
        "offset_out": out_off,
        "offset_in": in_off,
        "remaining": len(pad_bytes) - max(out_off, in_off),
    }


@app.post("/encrypt")
def encrypt(req: EncryptRequest):
    pad_bytes = load_pad(req.pad_id)
    packet = encrypt_message(
        req.pad_id,
        pad_bytes,
        req.message.encode()
    )

    return {
        "pad_id": packet.pad_id,
        "offset": packet.offset,
        "length": packet.length,
        "ciphertext": packet.ciphertext.hex()
    }

class ExportQRRequest(BaseModel):
    pad_id: str


class ImportQRRequest(BaseModel):
    frames_dir: str
    expected_hash: str | None = None

@app.post("/export_qr")
def export_qr(req: ExportQRRequest):
    output_dir, frame_count = export_pad_to_qr(req.pad_id)
    return {
        "output_dir": output_dir,
        "frames": frame_count,
    }


@app.post("/import_qr")
def import_qr(req: ImportQRRequest):
    pad_id = import_pad_from_qr(req.frames_dir, req.expected_hash)
    return {"pad_id": pad_id}