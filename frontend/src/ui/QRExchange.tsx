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
  const [qrImages, setQrImages] = useState<string[]>([]);

  const handleExport = async () => {
    if (!padId) {
      setError("No pad loaded to export");
      return;
    }

    try {
      setError(null);
      setStatus("Exporting...");

      const result = await exportPadToQR(padId, exportDir);

      setQrImages(result.images || []);
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
    <div className="card">
      <h2 style={{ marginTop: 0 }}>QR Pad Exchange</h2>

      <div className="grid-2">
        {/* Export Section */}
        <div style={{ padding: "1.5rem", background: "#f9fafb", borderRadius: "var(--radius)" }}>
          <h3 style={{ marginTop: 0 }}>Export Active Pad</h3>
          <div style={{ marginBottom: "1rem" }}>
            <label className="label">Output Directory</label>
            <input
              type="text"
              className="input-field"
              value={exportDir}
              onChange={(e) => setExportDir(e.target.value)}
            />
          </div>
          <button
            className="btn"
            onClick={handleExport}
            disabled={!padId}
            style={{ width: "100%" }}
          >
            Export to QR Frames
          </button>

          {qrImages.length > 0 && (
            <div style={{ marginTop: "1.5rem" }}>
              <h4 style={{ margin: "0 0 0.5rem 0" }}>Generated QR Frames</h4>
              <div style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(100px, 1fr))",
                gap: "0.5rem",
                maxHeight: "300px",
                overflowY: "auto",
                border: "1px solid var(--border-color)",
                padding: "0.5rem",
                borderRadius: "var(--radius)"
              }}>
                {qrImages.map((img) => (
                  <div key={img} style={{ textAlign: "center" }}>
                    <img
                      src={`http://localhost:9000/qr_images/${img}`}
                      alt={img}
                      style={{ width: "100%", borderRadius: "4px" }}
                    />
                    <div style={{ fontSize: "0.7rem", color: "var(--text-muted)", marginTop: "0.2rem" }}>
                      {img}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Import Section */}
        <div style={{ padding: "1.5rem", background: "#f9fafb", borderRadius: "var(--radius)" }}>
          <h3 style={{ marginTop: 0 }}>Import Pad from QR</h3>
          <div style={{ marginBottom: "1rem" }}>
            <label className="label">Frames Directory</label>
            <input
              type="text"
              className="input-field"
              value={importDir}
              onChange={(e) => setImportDir(e.target.value)}
            />
          </div>
          <div style={{ marginBottom: "1rem" }}>
            <label className="label">Expected Hash (Optional)</label>
            <input
              type="text"
              className="input-field"
              value={expectedHash}
              onChange={(e) => setExpectedHash(e.target.value)}
              placeholder="e.g. a3f9..."
            />
          </div>
          <button
            className="btn"
            onClick={handleImport}
            style={{ width: "100%", backgroundColor: "#059669" }}
          >
            Import & Verify
          </button>
        </div>
      </div>

      {(error || status) && (
        <div style={{
          marginTop: "1.5rem",
          padding: "1rem",
          borderRadius: "var(--radius)",
          backgroundColor: error ? "#fee2e2" : "#dcfce7",
          color: error ? "#991b1b" : "#166534"
        }}>
          {error && <div style={{ fontWeight: 600 }}>Error: {error}</div>}
          {status && !error && <div style={{ fontWeight: 600 }}>Status: {status}</div>}
        </div>
      )}
    </div>
  );
}