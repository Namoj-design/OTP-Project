// frontend/src/ui/QRExchange.tsx

import React, { useState } from "react";
import { exportPadToQR } from "../bridge/exchange";

export default function QRExchange({ padId }: { padId: string | null }) {
  const [status, setStatus] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleExport = async () => {
    if (!padId) {
      setError("No pad loaded");
      return;
    }

    try {
      setError(null);

      const result = await exportPadToQR(padId);

      setStatus(
        `Exported ${result.frame_count} frames to ${result.output_dir}`
      );
    } catch (err: any) {
      setError(err.message || "Failed to export QR frames");
    }
  };

  return (
    <div>
      <h3>QR Pad Exchange</h3>

      <button onClick={handleExport}>
        Export Pad to QR Frames
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {status && <p><b>Status:</b> {status}</p>}
    </div>
  );
}