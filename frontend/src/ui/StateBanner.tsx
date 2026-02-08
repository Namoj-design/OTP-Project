import React from "react";

export type AppState =
    | "NO_PAD"
    | "PAD_READY"
    | "MESSAGE_ENCRYPTED"
    | "MESSAGE_SENT"
    | "MESSAGE_RECEIVED"
    | "MESSAGE_DECRYPTED";

interface StateBannerProps {
    currentState: AppState;
    padId: string | null;
}

export default function StateBanner({ currentState, padId }: StateBannerProps) {
    const getColor = (s: AppState) => {
        switch (s) {
            case "NO_PAD": return "red";
            case "PAD_READY": return "green";
            default: return "blue";
        }
    };

    return (
        <div style={{
            padding: "1rem",
            backgroundColor: "#f0f0f0",
            borderBottom: "1px solid #ccc",
            marginBottom: "1rem",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center"
        }}>
            <div>
                <strong>Current State: </strong>
                <span style={{ color: getColor(currentState), fontWeight: "bold" }}>
                    {currentState}
                </span>
            </div>
            <div>
                <strong>Active Pad: </strong>
                {padId ? <code style={{ background: "#e0e0e0", padding: "2px 4px" }}>{padId}</code> : "None"}
            </div>
        </div>
    );
}