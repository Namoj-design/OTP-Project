// frontend/src/ui/PadManager.tsx

import React, { useState } from "react";
import { generatePad, getPadStatus, PadStatus } from "../bridge/pad";

export default function PadManager({
  onPadReady,
}: {
  onPadReady: (padId: string) => void;
}) {
  const [padStatus, setPadStatus] = useState<PadStatus | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleGenerate = async () => {
    try {
      setError(null);

      const result = await generatePad("data/sample_images/test.jpg");
      const status = await getPadStatus(result.pad_id);

      setPadStatus(status);
      onPadReady(result.pad_id);
    } catch (err: any) {
      setError(err.message || "Failed to generate pad");
    }
  };

  return (
    <div>
      <h3>Pad Manager</h3>

      <button onClick={handleGenerate}>
        Generate Pad (from entropy)
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {padStatus && (
        <div style={{ marginTop: "1rem" }}>
          <p><b>Pad ID:</b> {padStatus.pad_id}</p>
          <p><b>Pad Size:</b> {padStatus.pad_size}</p>
          <p><b>Pad Hash:</b> {padStatus.pad_hash}</p>
          <p><b>Offset Out:</b> {padStatus.offset_out}</p>
          <p><b>Offset In:</b> {padStatus.offset_in}</p>
          <p><b>Remaining:</b> {padStatus.remaining}</p>
        </div>
      )}
    </div>
  );
}