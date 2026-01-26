// frontend/src/bridge/pad.ts

const API_BASE = "http://127.0.0.1:9000";

export interface PadStatus {
  pad_id: string;
  pad_size: number;
  pad_hash: string;
  offset_out: number;
  offset_in: number;
  remaining: number;
}

export async function generatePad(imagePath: string) {
  const res = await fetch(`${API_BASE}/generate_pad`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image_path: imagePath }),
  });

  if (!res.ok) {
    throw new Error("Failed to generate pad");
  }

  return res.json();
}

export async function getPadStatus(padId: string): Promise<PadStatus> {
  const res = await fetch(`${API_BASE}/pad_status/${padId}`);

  if (!res.ok) {
    throw new Error("Failed to get pad status");
  }

  return res.json();
}