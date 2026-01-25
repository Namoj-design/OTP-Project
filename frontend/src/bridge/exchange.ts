export async function exportPadToQR(padId: string) {
    const res = await fetch("http://127.0.0.1:9000/export_qr", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pad_id: padId }),
    });
  
    return res.json();
  }
  
  export async function importPadFromQR(framesDir: string) {
    const res = await fetch("http://127.0.0.1:9000/import_qr", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ frames_dir: framesDir }),
    });
  
    return res.json();
  }