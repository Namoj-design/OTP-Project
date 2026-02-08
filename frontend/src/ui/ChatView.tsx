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
    <div className="grid-2">
      {/* Encryption Section */}
      <div className="card">
        <h2 style={{ marginTop: 0, color: "#2563eb" }}>Encrypt Message</h2>
        <div style={{ marginBottom: "1rem" }}>
          <label className="label">Plaintext Message</label>
          <textarea
            className="input-field"
            rows={5}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your secret message here..."
            style={{ resize: "vertical" }}
          />
        </div>

        <button
          className="btn"
          onClick={handleEncrypt}
          disabled={!padId || !message}
          style={{ width: "100%", background: "#2563eb" }}
        >
          Encrypt & Generate Packet
        </button>

        {packet && (
          <div style={{ marginTop: "1.5rem" }}>
            <label className="label">Encrypted Packet (JSON)</label>
            <div style={{
              background: "#1e293b",
              color: "#e2e8f0",
              padding: "1rem",
              borderRadius: "var(--radius)",
              fontSize: "0.85rem",
              position: "relative"
            }}>
              <pre style={{ margin: 0, whiteSpace: "pre-wrap", overflowX: "auto" }}>
                {JSON.stringify(packet, null, 2)}
              </pre>
              <button
                onClick={() => navigator.clipboard.writeText(JSON.stringify(packet))}
                style={{
                  position: "absolute",
                  top: "0.5rem",
                  right: "0.5rem",
                  background: "rgba(255,255,255,0.1)",
                  border: "none",
                  color: "white",
                  padding: "0.25rem 0.5rem",
                  borderRadius: "4px",
                  fontSize: "0.75rem"
                }}
              >
                Copy
              </button>
            </div>
            <p style={{ fontSize: "0.85rem", color: "var(--text-muted)", marginTop: "0.5rem" }}>
              Send this JSON packet to the recipient via any channel.
            </p>
          </div>
        )}
      </div>

      {/* Decryption Section */}
      <div className="card">
        <h2 style={{ marginTop: 0, color: "#7c3aed" }}>Decrypt Message</h2>
        <div style={{ marginBottom: "1rem" }}>
          <label className="label">Paste Packet JSON</label>
          <textarea
            className="input-field"
            rows={5}
            value={decryptInput}
            onChange={(e) => setDecryptInput(e.target.value)}
            placeholder='{"pad_id": "...", "ciphertext": "..."}'
            style={{ fontFamily: "monospace", fontSize: "0.9rem" }}
          />
        </div>

        <button
          className="btn"
          onClick={handleDecrypt}
          disabled={!padId || !decryptInput}
          style={{ width: "100%", background: "#7c3aed" }}
        >
          Decrypt Packet
        </button>

        {decryptedMessage && (
          <div style={{ marginTop: "1.5rem" }}>
            <label className="label">Decrypted Message</label>
            <div style={{
              padding: "1.5rem",
              background: "#ecfdf5",
              border: "1px solid #a7f3d0",
              borderRadius: "var(--radius)",
              color: "#065f46",
              fontSize: "1.1rem",
              lineHeight: "1.6"
            }}>
              {decryptedMessage}
            </div>
          </div>
        )}

        {error && (
          <div style={{ marginTop: "1rem", color: "#dc2626", background: "#fef2f2", padding: "1rem", borderRadius: "var(--radius)" }}>
            <b>Error:</b> {error}
          </div>
        )}
      </div>
    </div>
  );
}