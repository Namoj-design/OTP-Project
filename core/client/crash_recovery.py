# core/client/crash_recovery.py

from core.client.offset_store import load_offsets


def recover_offsets(pad_id: str):
    return load_offsets(pad_id)