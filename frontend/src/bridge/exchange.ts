export async function importPadFromQR(framesDir: string, expectedHash?: string) {
  const res = await fetch("http://127.0.0.1:9000/import_qr", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      frames_dir: framesDir,
      expected_hash: expectedHash || null,
    }),
  });

  if (!res.ok) throw new Error("import_qr failed");
  return await res.json();
}