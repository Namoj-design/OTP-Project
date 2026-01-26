import { useState } from "react";
import { captureEntropyAndGeneratePad } from "../bridge/entropy";
import { getPadStatus, PadStatus } from "../bridge/pad";
import { exportPadToQR } from "../bridge/exchange";

export default function PadManager() {
  const [padStatus, setPadStatus] = useState<PadStatus | null>(null);
  const [status, setStatus] = useState<string>("");

  const handleGenerate = async () => {
    try {
      const result = await captureEntropyAndGeneratePad();
      const status = await getPadStatus(result.pad_id);
      setPadStatus(status);
      setStatus("Pad generated");
    } catch {
      setStatus("Failed to generate pad");
    }
  };

  const handleExport = async () => {
    if (!padStatus) return;

    try {
      const result = await exportPadToQR(padStatus.pad_id);
      setStatus(`Exported ${result.frame_count} frames to ${result.frames_dir}`);
    } catch {
      setStatus("Failed to export pad to QR");
    }
  };

  return (
    <div>
      <h2>Pad Manager</h2>

      <button onClick={handleGenerate}>Generate Pad (from entropy)</button>

      {padStatus && (
        <div>
          <p><b>Pad ID:</b> {padStatus.pad_id}</p>
          <p><b>Pad Size:</b> {padStatus.pad_size}</p>
          <p><b>Pad Hash:</b> {padStatus.pad_hash}</p>
          <p><b>Offset Out:</b> {padStatus.offset_out}</p>
          <p><b>Offset In:</b> {padStatus.offset_in}</p>
          <p><b>Remaining:</b> {padStatus.remaining}</p>
        </div>
      )}

      <h3>QR Pad Exchange</h3>
      <button onClick={handleExport}>Export Pad to QR Frames</button>

      {status && <p>{status}</p>}
    </div>
  );
}