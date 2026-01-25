# backend/routes.py

from fastapi import APIRouter
from backend.storage import store_message, fetch_messages
from backend.models import SendMessageRequest

router = APIRouter()


@router.post("/send")
def send_message(req: SendMessageRequest):
    store_message(
        pad_id=req.pad_id,
        sender=req.sender,
        recipient=req.recipient,
        packet=req.packet
    )

    return {"status": "stored"}


@router.get("/fetch/{recipient}")
def fetch(recipient: str):
    rows = fetch_messages(recipient)

    messages = []
    for msg_id, pad_id, sender, packet in rows:
        messages.append({
            "id": msg_id,
            "pad_id": pad_id,
            "sender": sender,
            "packet": packet
        })

    return {"messages": messages}