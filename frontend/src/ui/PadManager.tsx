import { useState } from "react";
import { generatePad } from "../bridge/pad";
import { getPadStatus, PadStatus } from "../bridge/pad";

interface PadManagerProps {
  onPadReady: (padId: string) => void;
}

export default function PadManager({ onPadReady }: PadManagerProps) {
  const [padStatus, setPadStatus] = useState<PadStatus | null>(null);
  const [status, setStatus] = useState<string>("");
  const [imagePath, setImagePath] = useState<string>("data/sample_images/test.jpg");
  const [owner, setOwner] = useState<string>("local-user");

  const handleGenerate = async () => {
    try {
      setStatus("Generating pad from entropy...");
      const result = await generatePad(imagePath, owner);
      const status = await getPadStatus(result.pad_id);

      setPadStatus(status);
      setStatus("Pad generated successfully!");
      onPadReady(result.pad_id);
    } catch (e: any) {
      setStatus("Failed to generate pad: " + e.message);
    }
  };

  return (
    <div style={{ padding: "1rem", border: "1px solid #ccc", borderRadius: "8px", marginBottom: "2rem" }}>
      <h2>Pad Manager</h2>

      <div style={{ marginBottom: "1rem" }}>
        <label style={{ display: "block", marginBottom: "0.5rem" }}>Entropy Source Image Path:</label>
        <input
          type="text"
          value={imagePath}
          onChange={(e) => setImagePath(e.target.value)}
          style={{ width: "100%", padding: "0.5rem" }}
        />
      </div>

      <div style={{ marginBottom: "1rem" }}>
        <label style={{ display: "block", marginBottom: "0.5rem" }}>Owner ID:</label>
        <input
          type="text"
          value={owner}
          onChange={(e) => setOwner(e.target.value)}
          style={{ width: "100%", padding: "0.5rem" }}
        />
      </div>

      <button
        onClick={handleGenerate}
        style={{ padding: "0.5rem 1rem", backgroundColor: "#007bff", color: "white", border: "none", borderRadius: "4px", cursor: "pointer" }}
      >
        Generate Pad (from entropy)
      </button>

      {status && <p style={{ marginTop: "1rem", fontWeight: "bold" }}>{status}</p>}

      {padStatus && (
        <div style={{ marginTop: "1rem", backgroundColor: "#f8f9fa", padding: "1rem", borderRadius: "4px" }}>
          <h3 style={{ marginTop: 0 }}>Active Pad Status</h3>
          <div style={{ display: "grid", gridTemplateColumns: "auto 1fr", gap: "0.5rem 1rem" }}>
            <b>Pad ID:</b> <code>{padStatus.pad_id}</code>
            <b>Size:</b> <span>{padStatus.pad_size} bytes</span>
            <b>Offset Out:</b> <span>{padStatus.offset_out}</span>
            <b>Offset In:</b> <span>{padStatus.offset_in}</span>
            <b>Remaining:</b> <span>{padStatus.remaining} bytes</span>
          </div>
          <div style={{ marginTop: "0.5rem" }}>
            <b>Hash:</b> <code style={{ wordBreak: "break-all" }}>{padStatus.pad_hash}</code>
          </div>
        </div>
      )}
    </div>
  );
}