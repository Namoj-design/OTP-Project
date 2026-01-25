# backend/storage.py

import sqlite3
from backend.config import DATABASE_PATH


def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pad_id TEXT NOT NULL,
            sender TEXT NOT NULL,
            recipient TEXT NOT NULL,
            packet BLOB NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def store_message(pad_id: str, sender: str, recipient: str, packet: bytes):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()

    c.execute(
        "INSERT INTO messages (pad_id, sender, recipient, packet) VALUES (?, ?, ?, ?)",
        (pad_id, sender, recipient, packet)
    )

    conn.commit()
    conn.close()


def fetch_messages(recipient: str):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()

    c.execute(
        "SELECT id, pad_id, sender, packet FROM messages WHERE recipient = ? ORDER BY id",
        (recipient,)
    )

    rows = c.fetchall()

    # delete after fetch (one-time delivery)
    c.execute(
        "DELETE FROM messages WHERE recipient = ?",
        (recipient,)
    )

    conn.commit()
    conn.close()

    return rows