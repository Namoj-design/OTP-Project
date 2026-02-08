// frontend/src/bridge/exchange.ts

const API_BASE = "http://127.0.0.1:9000";

export async function exportPadToQR(padId: string, outputDir: string = "data/qr_frames") {
  const res = await fetch(`${API_BASE}/export_qr`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pad_id: padId,
      output_dir: outputDir
    }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`export_qr failed: ${text}`);
  }

  return await res.json() as {
    frames_dir: string;
    frame_count: number;
  };
}

export async function importPadFromQR(
  framesDir: string,
  expectedHash?: string
) {
  const res = await fetch(`${API_BASE}/import_qr`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      frames_dir: framesDir,
      expected_hash: expectedHash ?? null,
    }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`import_qr failed: ${text}`);
  }

  return await res.json() as {
    pad_id: string;
    pad_hash: string;
    pad_size: number;
  };
}