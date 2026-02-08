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
    <div className="card">
      <h2 style={{ marginTop: 0 }}>Pad Manager</h2>

      <div className="grid-2">
        <div>
          <label className="label">Entropy Source Image Path</label>
          <input
            type="text"
            className="input-field"
            value={imagePath}
            onChange={(e) => setImagePath(e.target.value)}
          />
        </div>

        <div>
          <label className="label">Owner ID</label>
          <input
            type="text"
            className="input-field"
            value={owner}
            onChange={(e) => setOwner(e.target.value)}
          />
        </div>
      </div>

      <div style={{ marginTop: "1.5rem" }}>
        <button className="btn" onClick={handleGenerate}>
          Generate Pad (from entropy)
        </button>
      </div>

      {status && (
        <div style={{
          marginTop: "1.5rem",
          padding: "1rem",
          background: status.includes("Fail") ? "#fee2e2" : "#dcfce7",
          color: status.includes("Fail") ? "#991b1b" : "#166534",
          borderRadius: "var(--radius)"
        }}>
          <b>Status:</b> {status}
        </div>
      )}

      {padStatus && (
        <div style={{
          marginTop: "1.5rem",
          backgroundColor: "#f9fafb",
          padding: "1.5rem",
          borderRadius: "var(--radius)",
          border: "1px solid var(--border-color)"
        }}>
          <h3 style={{ marginTop: 0, fontSize: "1.1rem" }}>Active Pad Status</h3>
          <div style={{ display: "grid", gridTemplateColumns: "auto 1fr", gap: "0.5rem 1.5rem", alignItems: "baseline" }}>
            <span style={{ color: "var(--text-muted)" }}>Pad ID:</span>
            <code>{padStatus.pad_id}</code>

            <span style={{ color: "var(--text-muted)" }}>Size:</span>
            <span>{padStatus.pad_size.toLocaleString()} bytes</span>

            <span style={{ color: "var(--text-muted)" }}>Remaining:</span>
            <span style={{ color: padStatus.remaining < 1000 ? "#dc2626" : "inherit", fontWeight: "600" }}>
              {padStatus.remaining.toLocaleString()} bytes
            </span>

            <span style={{ color: "var(--text-muted)" }}>Offsets:</span>
            <span>Out: {padStatus.offset_out} / In: {padStatus.offset_in}</span>
          </div>
          <div style={{ marginTop: "1rem" }}>
            <div style={{ color: "var(--text-muted)", marginBottom: "0.25rem", fontSize: "0.9em" }}>Hash</div>
            <code style={{ wordBreak: "break-all", fontSize: "0.8em", display: "block" }}>{padStatus.pad_hash}</code>
          </div>
        </div>
      )}
    </div>
  );
}