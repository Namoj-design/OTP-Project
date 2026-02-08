export type PadStatus = {
  pad_id: string;
  pad_size: number;
  pad_hash: string;
  offset_out: number;
  offset_in: number;
  remaining: number;
};

export async function generatePad(imagePath: string, owner: string = "local-user") {
  const res = await fetch("http://127.0.0.1:9000/generate_pad", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      image_path: imagePath,
      owner: owner
    }),
  });

  if (!res.ok) throw new Error("generate_pad failed");

  return await res.json();
}

export async function getPadStatus(padId: string): Promise<PadStatus> {
  const res = await fetch(`http://127.0.0.1:9000/pad_status/${padId}`);
  if (!res.ok) throw new Error("pad_status failed");
  return await res.json();
}