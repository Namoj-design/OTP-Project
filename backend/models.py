# backend/models.py

from pydantic import BaseModel


class SendMessageRequest(BaseModel):
    pad_id: str
    sender: str
    recipient: str
    packet: bytes