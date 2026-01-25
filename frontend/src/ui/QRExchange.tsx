import React, { useState } from "react";
import {
  exportPadToQR,
  importPadFromQR,
} from "../bridge/exchange";

export default function QRExchange({
  padId,
  onPadImported,
}: {
  padId: string | null;
  onPadImported: (padId: string) => void;
}) {
  const [status, setStatus] = useState<string | null>(null);
  const [framesDir, setFramesDir] = useState("");
  const [expectedHash, setExpectedHash] = useState("");

  const handleExport = async () => {
    if (!padId) {
      alert("No active pad to export.");
      return;
    }

    const result = await exportPadToQR(padId);
    setStatus(
      `Exported ${result.frames} frames to ${result.output_dir}`
    );
  };

  const handleImport = async () => {
    if (!framesDir) {
      alert("Enter frames directory path.");
      return;
    }

    const result = await importPadFromQR(
      framesDir,
      expectedHash || undefined
    );

    setStatus(`Imported pad: ${result.pad_id}`);
    onPadImported(result.pad_id);
  };

  return (
    <div style={{ marginTop: "2rem" }}>
      <h3>QR Pad Exchange</h3>

      <button onClick={handleExport}>
        Export Pad to QR Frames
      </button>

      <div style={{ marginTop: "1rem" }}>
        <input
          type="text"
          placeholder="Path to QR frames directory"
          value={framesDir}
          onChange={(e) => setFramesDir(e.target.value)}
          style={{ width: "400px" }}
        />
        <input
          type="text"
          placeholder="Expected pad hash (optional)"
          value={expectedHash}
          onChange={(e) => setExpectedHash(e.target.value)}
          style={{ width: "400px" }}
        />
        <br /><br />
        <button onClick={handleImport}>
          Import Pad from QR Frames
        </button>
      </div>

      {status && (
        <p style={{ marginTop: "1rem" }}>
          <b>Status:</b> {status}
        </p>
      )}
    </div>
  );
}