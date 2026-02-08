import React from "react";

export type AppState =
    | "NO_PAD"
    | "PAD_LOADED"
    | "PAD_READY"
    | "ENCRYPTING"
    | "DECRYPTING"
    | "MESSAGE_ENCRYPTED"
    | "MESSAGE_DECRYPTED";

interface Props {
    currentState: AppState;
    padId: string | null;
}

export default function StateBanner({ currentState, padId }: Props) {
    const getStatusConfig = () => {
        switch (currentState) {
            case "NO_PAD":
                return { color: "#6b7280", bg: "#f3f4f6", label: "System Idle • No Pad" };
            case "PAD_LOADED":
                return { color: "#d97706", bg: "#fef3c7", label: "Pad Loaded • Initializing" };
            case "PAD_READY":
                return { color: "#059669", bg: "#dcfce7", label: "Secure Channel Ready" };
            case "ENCRYPTING":
                return { color: "#2563eb", bg: "#dbeafe", label: "Encrypting..." };
            case "DECRYPTING":
                return { color: "#7c3aed", bg: "#ede9fe", label: "Decrypting..." };
            case "MESSAGE_ENCRYPTED":
                return { color: "#2563eb", bg: "#dbeafe", label: "Message Encrypted & Packet Ready" };
            case "MESSAGE_DECRYPTED":
                return { color: "#7c3aed", bg: "#ede9fe", label: "Message Decrypted Successfully" };
            default:
                return { color: "#6b7280", bg: "#f3f4f6", label: "Unknown State" };
        }
    };

    const config = getStatusConfig();

    return (
        <div style={{
            marginBottom: "2rem",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            background: "var(--surface-color)",
            padding: "0.75rem 1.5rem",
            borderRadius: "9999px",
            boxShadow: "var(--shadow-sm)",
            border: "1px solid var(--border-color)"
        }}>
            <div style={{ display: "flex", alignItems: "center", gap: "0.75rem" }}>
                <div style={{
                    width: "12px",
                    height: "12px",
                    borderRadius: "50%",
                    backgroundColor: config.color,
                    boxShadow: `0 0 0 2px ${config.bg}`
                }} />
                <span style={{ fontWeight: 600, color: config.color }}>{config.label}</span>
            </div>

            <div style={{ fontSize: "0.9rem", color: "var(--text-muted)", display: "flex", alignItems: "center", gap: "0.5rem" }}>
                <span>Active Pad:</span>
                {padId ? (
                    <code style={{ background: "#f3f4f6", padding: "0.2rem 0.6rem", borderRadius: "6px" }}>
                        {padId}
                    </code>
                ) : (
                    <span style={{ fontStyle: "italic" }}>None</span>
                )}
            </div>
        </div>
    );
}