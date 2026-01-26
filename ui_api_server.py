# ui_api_server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.api.pad_api import generate_pad_from_image, load_pad

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GeneratePadRequest(BaseModel):
    image_path: str


@app.post("/generate_pad")
def generate_pad(req: GeneratePadRequest):
    result = generate_pad_from_image(req.image_path)

    return {
        "pad_id": result["pad_id"],
        "pad_size": result["pad_size"],
        "pad_hash": result["pad_hash"],
    }


@app.get("/pad_status/{pad_id}")
def pad_status(pad_id: str):
    status = load_pad(pad_id)
    return status