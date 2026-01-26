// frontend/src/bridge/exchange.ts

const API_BASE = "http://127.0.0.1:9000";

export async function exportPadToQR(padId: string) {
  const res = await fetch(`${API_BASE}/export_qr`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pad_id: padId }),
  });

  if (!res.ok) {
    throw new Error("Failed to export pad to QR");
  }

  return res.json();
}