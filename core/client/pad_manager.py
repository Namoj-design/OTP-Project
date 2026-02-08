# core/client/pad_manager.py

from core.crypto.pad_state import PadState
from core.client.offset_store import load_offsets, save_offsets


class PadManager:
    def __init__(self, pad_id: str, pad_bytes: bytes):
        self.pad_id = pad_id
        self.pad_bytes = pad_bytes

        out, inc = load_offsets(pad_id)

        self.state = PadState(pad_bytes)
        self.state.offset_out = out
        self.state.offset_in = inc

    def persist(self):
        # Save to atomic offset store
        save_offsets(
            self.pad_id,
            self.state.offset_out,
            self.state.offset_in
        )
        
        # Also update registry for visibility
        from core.pad.pad_registry import update_offsets
        update_offsets(
            self.pad_id,
            offset_in=self.state.offset_in,
            offset_out=self.state.offset_out
        )