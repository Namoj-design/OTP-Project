# ui_api_server.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.api.pad_api import generate_pad_from_image, pad_status
from core.api.exchange_api import export_pad_to_qr, import_pad_from_qr
from core.api.message_api import encrypt_message, decrypt_message
from core.pad.pad_loader import load_pad_bytes
from core.protocol.message import MessagePacket

app = FastAPI(title="OTP Secure Messaging API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GeneratePadRequest(BaseModel):
    image_path: str
    owner: str = "local-user"

class ExportQRRequest(BaseModel):
    pad_id: str
    output_dir: str = "data/qr_frames"

class ImportQRRequest(BaseModel):
    frames_dir: str
    expected_hash: str | None = None

class EncryptRequest(BaseModel):
    pad_id: str
    message: str

class DecryptRequest(BaseModel):
    pad_id: str
    ciphertext: str
    offset: int
    length: int

@app.post("/generate_pad")
def generate_pad(req: GeneratePadRequest):
    try:
        result = generate_pad_from_image(req.image_path, req.owner)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pad_status/{pad_id}")
def get_status(pad_id: str):
    try:
        result = pad_status(pad_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/export_qr")
def export_qr(req: ExportQRRequest):
    try:
        result = export_pad_to_qr(req.pad_id, req.output_dir)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/import_qr")
def import_qr(req: ImportQRRequest):
    try:
        result = import_pad_from_qr(req.frames_dir, req.expected_hash)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/encrypt")
def encrypt(req: EncryptRequest):
    try:
        pad_bytes = load_pad_bytes(req.pad_id)
        plaintext = req.message.encode('utf-8')
        packet = encrypt_message(req.pad_id, pad_bytes, plaintext)
        
        return {
            "ciphertext": packet.ciphertext.hex(),
            "offset": packet.offset,
            "length": packet.length
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/decrypt")
def decrypt(req: DecryptRequest):
    try:
        pad_bytes = load_pad_bytes(req.pad_id)
        ciphertext = bytes.fromhex(req.ciphertext)
        
        packet = MessagePacket(
            pad_id=req.pad_id,
            offset=req.offset,
            length=req.length,
            ciphertext=ciphertext
        )
        
        plaintext = decrypt_message(req.pad_id, pad_bytes, packet)
        
        return {
            "plaintext": plaintext.decode('utf-8')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))