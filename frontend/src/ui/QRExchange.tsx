// frontend/src/ui/QRExchange.tsx

import React, { useState } from "react";
import { exportPadToQR, importPadFromQR } from "../bridge/exchange";

interface QRExchangeProps {
  padId: string | null;
  onPadImported: (padId: string) => void;
}

export default function QRExchange({ padId, onPadImported }: QRExchangeProps) {
  const [status, setStatus] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [exportDir, setExportDir] = useState("data/qr_frames");
  const [importDir, setImportDir] = useState("data/qr_frames");
  const [expectedHash, setExpectedHash] = useState("");

  const handleExport = async () => {
    if (!padId) {
      setError("No pad loaded to export");
      return;
    }

    try {
      setError(null);
      setStatus("Exporting...");

      const result = await exportPadToQR(padId, exportDir);

      setStatus(
        `Exported ${result.frame_count} frames to ${result.frames_dir}`
      );
    } catch (err: any) {
      setError(err.message || "Failed to export QR frames");
    }
  };

  const handleImport = async () => {
    try {
      setError(null);
      setStatus("Importing & Verifying...");

      const result = await importPadFromQR(importDir, expectedHash || undefined);

      setStatus(`Successfully imported pad ${result.pad_id.slice(0, 8)}... (${result.pad_size} bytes)`);
      onPadImported(result.pad_id);
    } catch (err: any) {
      setError("Import failed: " + err.message);
    }
  };

  return (
    <div style={{ padding: "1rem", border: "1px solid #ccc", borderRadius: "8px", marginBottom: "2rem" }}>
      <h2>QR Pad Exchange</h2>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "2rem" }}>
        {/* Export Section */}
        <div>
          <h3>Export Active Pad</h3>
          <div style={{ marginBottom: "0.5rem" }}>
            <label style={{ display: "block", marginBottom: "0.25rem" }}>Output Directory:</label>
            <input
              type="text"
              value={exportDir}
              onChange={(e) => setExportDir(e.target.value)}
              style={{ width: "100%", padding: "0.25rem" }}
            />
          </div>
          <button
            onClick={handleExport}
            disabled={!padId}
            style={{ padding: "0.5rem 1rem", cursor: "pointer" }}
          >
            Export to QR Frames
          </button>
        </div>

        {/* Import Section */}
        <div>
          <h3>Import Pad from QR</h3>
          <div style={{ marginBottom: "0.5rem" }}>
            <label style={{ display: "block", marginBottom: "0.25rem" }}>Frames Directory:</label>
            <input
              type="text"
              value={importDir}
              onChange={(e) => setImportDir(e.target.value)}
              style={{ width: "100%", padding: "0.25rem" }}
            />
          </div>
          <div style={{ marginBottom: "0.5rem" }}>
            <label style={{ display: "block", marginBottom: "0.25rem" }}>Expected Hash (Optional):</label>
            <input
              type="text"
              value={expectedHash}
              onChange={(e) => setExpectedHash(e.target.value)}
              placeholder="SHA256 hash..."
              style={{ width: "100%", padding: "0.25rem" }}
            />
          </div>
          <button
            onClick={handleImport}
            style={{ padding: "0.5rem 1rem", cursor: "pointer" }}
          >
            Import & Verify
          </button>
        </div>
      </div>

      {(error || status) && (
        <div style={{ marginTop: "1rem", padding: "0.5rem", borderRadius: "4px", backgroundColor: error ? "#ffebee" : "#e8f5e9" }}>
          {error && <p style={{ color: "#c62828", margin: 0 }}><b>Error:</b> {error}</p>}
          {status && !error && <p style={{ color: "#2e7d32", margin: 0 }}><b>Status:</b> {status}</p>}
        </div>
      )}
    </div>
  );
}