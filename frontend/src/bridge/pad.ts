export type PadStatus = {
  pad_id: string;
  pad_size: number;
  pad_hash: string;
};

export async function generatePad(imagePath: string): Promise<PadStatus> {
  const res = await fetch("http://127.0.0.1:9000/generate_pad", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image_path: imagePath }),
  });

  if (!res.ok) {
    throw new Error(`generatePad failed: ${res.status}`);
  }

  return res.json();
}

export async function getPadStatus(padId: string): Promise<PadStatus> {
  const res = await fetch(
    `http://127.0.0.1:9000/pad_status/${padId}`
  );

  if (!res.ok) {
    throw new Error(`getPadStatus failed: ${res.status}`);
  }

  return res.json();
}