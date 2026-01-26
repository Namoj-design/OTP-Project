export async function exportPadToQR(padId: string) {
  const res = await fetch("http://127.0.0.1:9000/export_qr", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pad_id: padId }),
  });

  if (!res.ok) throw new Error("export_qr failed");

  return await res.json();
}