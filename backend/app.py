# backend/app.py

from fastapi import FastAPI
from backend.routes import router
from backend.storage import init_db

app = FastAPI(title="OTP Mailbox Server")

init_db()
app.include_router(router)