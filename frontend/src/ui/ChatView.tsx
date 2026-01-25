import React, { useState } from "react";
import { encryptMessage } from "../bridge/message";
import { EncryptedPacket } from "../types/protocol";

export default function ChatView({
  padId,
}: {
  padId: string | null;
}) {
  const [message, setMessage] = useState("");
  const [packet, setPacket] = useState<EncryptedPacket | null>(null);

  const handleEncrypt = async () => {
    if (!padId) {
      alert("No active pad.");
      return;
    }

    const result = await encryptMessage(padId, message);
    setPacket(result);
  };

  return (
    <div>
      <h3>Chat</h3>

      <textarea
        rows={4}
        cols={50}
        placeholder="Type message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <br /><br />

      <button onClick={handleEncrypt}>
        Encrypt Message
      </button>

      {packet && (
        <div style={{ marginTop: "1rem" }}>
          <p><b>Offset:</b> {packet.offset}</p>
          <p><b>Length:</b> {packet.length}</p>
          <p><b>Ciphertext:</b></p>
          <code>{packet.ciphertext}</code>
        </div>
      )}
    </div>
  );
}