import React, { useState } from "react";
import { encryptMessage, decryptMessage } from "../bridge/message";
import { EncryptedPacket } from "../types/protocol";
import { AppState } from "./StateBanner";

interface ChatViewProps {
  padId: string | null;
  onStateChange: (state: AppState) => void;
}

export default function ChatView({ padId, onStateChange }: ChatViewProps) {
  const [message, setMessage] = useState("");
  const [packet, setPacket] = useState<EncryptedPacket | null>(null);
  const [decryptInput, setDecryptInput] = useState("");
  const [decryptedMessage, setDecryptedMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleEncrypt = async () => {
    setError(null);
    if (!padId) {
      setError("No active pad selected");
      return;
    }

    try {
      const result = await encryptMessage(padId, message);
      setPacket(result);
      onStateChange("MESSAGE_ENCRYPTED");
    } catch (e: any) {
      setError(e.message);
    }
  };

  const handleDecrypt = async () => {
    setError(null);
    if (!padId) {
      setError("No active pad selected");
      return;
    }

    try {
      // Parse the JSON packet from input
      let parsed;
      try {
        parsed = JSON.parse(decryptInput);
      } catch {
        setError("Invalid JSON packet format");
        return;
      }

      const result = await decryptMessage(
        padId,
        parsed.ciphertext,
        parsed.offset,
        parsed.length
      );

      setDecryptedMessage(result.plaintext);
      onStateChange("MESSAGE_DECRYPTED");
    } catch (e: any) {
      setError("Decryption failed: " + e.message);
    }
  };

  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "2rem" }}>
      {/* Encryption Side */}
      <div style={{ border: "1px solid #ddd", padding: "1rem", borderRadius: "8px" }}>
        <h3>Encrypt Message</h3>
        <textarea
          rows={4}
          style={{ width: "100%", marginBottom: "1rem" }}
          placeholder="Type secret message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button
          onClick={handleEncrypt}
          disabled={!padId || !message}
          style={{ padding: "0.5rem 1rem", cursor: "pointer" }}
        >
          Encrypt
        </button>

        {packet && (
          <div style={{ marginTop: "1rem", background: "#f8f9fa", padding: "0.5rem", borderRadius: "4px" }}>
            <h4>Encrypted Packet (Copy this):</h4>
            <pre style={{ whiteSpace: "pre-wrap", wordBreak: "break-all", fontSize: "0.85rem" }}>
              {JSON.stringify(packet, null, 2)}
            </pre>
            <div style={{ marginTop: "0.5rem", fontSize: "0.8rem", color: "#666" }}>
              Offset: {packet.offset} | Length: {packet.length}
            </div>
          </div>
        )}
      </div>

      {/* Decryption Side */}
      <div style={{ border: "1px solid #ddd", padding: "1rem", borderRadius: "8px" }}>
        <h3>Decrypt Packet</h3>
        <textarea
          rows={4}
          style={{ width: "100%", marginBottom: "1rem" }}
          placeholder="Paste JSON packet here..."
          value={decryptInput}
          onChange={(e) => setDecryptInput(e.target.value)}
        />
        <button
          onClick={handleDecrypt}
          disabled={!padId || !decryptInput}
          style={{ padding: "0.5rem 1rem", cursor: "pointer" }}
        >
          Decrypt
        </button>

        {decryptedMessage && (
          <div style={{ marginTop: "1rem", background: "#e3f2fd", padding: "1rem", borderRadius: "4px", border: "1px solid #90caf9" }}>
            <h4 style={{ margin: "0 0 0.5rem 0", color: "#1565c0" }}>Decrypted Message:</h4>
            <div style={{ fontSize: "1.1rem" }}>{decryptedMessage}</div>
          </div>
        )}
      </div>

      {error && (
        <div style={{ gridColumn: "1 / -1", color: "red", marginTop: "1rem", textAlign: "center" }}>
          {error}
        </div>
      )}
    </div>
  );
}