import React, { useState } from "react";
import { captureEntropyAndGeneratePad } from "../bridge/entropy";
import { getPadStatus } from "../bridge/pad";
import { PadStatus } from "../types/protocol";

export default function PadManager({
  onPadReady,
}: {
  onPadReady: (padId: string) => void;
}) {
  const [padStatus, setPadStatus] = useState<PadStatus | null>(null);

  const handleGenerate = async () => {
    const result = await captureEntropyAndGeneratePad();
    const status = await getPadStatus(result.pad_id);

    setPadStatus(status);
    onPadReady(result.pad_id);
  };

  return (
    <div>
      <h3>Pad Manager</h3>

      <button onClick={handleGenerate}>
        Generate Pad (from entropy)
      </button>

      {padStatus && (
        <div style={{ marginTop: "1rem" }}>
          <p><b>Pad ID:</b> {padStatus.pad_id}</p>
          <p><b>Pad Size:</b> {padStatus.pad_size}</p>
          <p><b>Offset Out:</b> {padStatus.offset_out}</p>
          <p><b>Offset In:</b> {padStatus.offset_in}</p>
          <p><b>Remaining:</b> {padStatus.remaining}</p>
        </div>
      )}
    </div>
  );
}