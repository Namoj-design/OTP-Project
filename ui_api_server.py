# ui_api_server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.api.pad_api import generate_pad_from_image, pad_status
from core.api.exchange_api import export_pad_to_qr, import_pad_from_qr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class GeneratePadRequest(BaseModel):
    image_path: str

class ExportQRRequest(BaseModel):
    pad_id: str

class ImportQRRequest(BaseModel):
    frames_dir: str
    expected_hash: str | None = None

@app.post("/generate_pad")
def generate_pad(req: GeneratePadRequest):
    return generate_pad_from_image(req.image_path)

@app.get("/pad_status/{pad_id}")
def get_status(pad_id: str):
    return pad_status(pad_id)

@app.post("/export_qr")
def export_qr(req: ExportQRRequest):
    return export_pad_to_qr(req.pad_id)

@app.post("/import_qr")
def import_qr(req: ImportQRRequest):
    return import_pad_from_qr(req.frames_dir, req.expected_hash)