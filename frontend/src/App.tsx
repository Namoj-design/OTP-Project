import React, { useState } from "react";
import PadManager from "./ui/PadManager";
import ChatView from "./ui/ChatView";
import QRExchange from "./ui/QRExchange";
import StateBanner, { AppState } from "./ui/StateBanner";

export default function App() {
  const [activePadId, setActivePadId] = useState<string | null>(null);
  const [appState, setAppState] = useState<AppState>("NO_PAD");

  const handlePadReady = (padId: string) => {
    setActivePadId(padId);
    setAppState("PAD_READY");
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif", maxWidth: "1200px", margin: "0 auto" }}>
      <h1 style={{ textAlign: "center", marginBottom: "2rem" }}>OTP Secure Messenger</h1>

      <StateBanner currentState={appState} padId={activePadId} />

      <PadManager onPadReady={handlePadReady} />

      <QRExchange
        padId={activePadId}
        onPadImported={handlePadReady}
      />

      <hr style={{ margin: "2rem 0" }} />

      <ChatView
        padId={activePadId}
        onStateChange={setAppState}
      />
    </div>
  );
}