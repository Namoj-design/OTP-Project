export async function encryptMessage(padId: string, message: string) {
  const res = await fetch("http://127.0.0.1:9000/encrypt", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pad_id: padId,
      message: message,
    }),
  });

  if (!res.ok) throw new Error("encrypt failed");

  return res.json();
}

export async function decryptMessage(
  padId: string,
  ciphertext: string,
  offset: number,
  length: number
) {
  const res = await fetch("http://127.0.0.1:9000/decrypt", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pad_id: padId,
      ciphertext: ciphertext,
      offset: offset,
      length: length,
    }),
  });

  if (!res.ok) throw new Error("decrypt failed");

  return res.json();
}