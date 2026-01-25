export async function generatePad(imagePath: string) {
    const res = await fetch("http://127.0.0.1:9000/generate_pad", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image_path: imagePath }),
    });
  
    return res.json();
  }
  
  export async function getPadStatus(padId: string) {
    const res = await fetch(
      `http://127.0.0.1:9000/pad_status/${padId}`
    );
  
    return res.json();
  }