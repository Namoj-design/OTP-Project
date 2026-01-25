import React, { useState } from "react";
import PadManager from "./ui/PadManager";
import ChatView from "./ui/ChatView";

export default function App() {
  const [activePadId, setActivePadId] = useState<string | null>(null);

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h2>OTP Secure Messenger</h2>

      <PadManager onPadReady={setActivePadId} />

      <hr />

      <ChatView padId={activePadId} />
    </div>
  );
}