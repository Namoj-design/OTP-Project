export async function encryptMessage(padId: string, message: string) {
    const res = await fetch("http://127.0.0.1:9000/encrypt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        pad_id: padId,
        message: message,
      }),
    });
  
    return res.json();
  }