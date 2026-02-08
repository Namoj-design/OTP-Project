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
    <div className="container">
      <header style={{ marginBottom: "3rem", textAlign: "center" }}>
        <h1 style={{
          fontSize: "2.5rem",
          fontWeight: "800",
          background: "linear-gradient(to right, #4f46e5, #06b6d4)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent",
          margin: 0
        }}>
          OTP Secure Messenger
        </h1>
        <p style={{ color: "var(--text-muted)", marginTop: "0.5rem" }}>
          Shannon Perfect Secrecy • Air-Gapped • Crash-Safe
        </p>
      </header>

      <StateBanner currentState={appState} padId={activePadId} />

      <PadManager onPadReady={handlePadReady} />

      <QRExchange
        padId={activePadId}
        onPadImported={handlePadReady}
      />

      <ChatView
        padId={activePadId}
        onStateChange={setAppState}
      />
    </div>
  );
}