# OTP Secure Messaging System

An academically correct One-Time Pad (OTP) secure messaging system with strict lifecycle discipline, replay protection, and air-gapped QR-based pad transfer.

## Features

- **Shannon Perfect Secrecy**: Strict one-time pad usage with no reuse.
- **Hardware Entropy**: Camera-based entropy collection with Von Neumann extraction.
- **Air-Gapped Exchange**: QR code pipelining for secure pad transfer between devices.
- **Crash-Safe**: Atomic offset persistence and registry management.
- **Modern UI**: React + TypeScript frontend with real-time state visualization.

## Prerequisites

- Python 3.10+
- Node.js 18+
- Webcam (for entropy generation)

## Setup

### 1. Backend Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn ui_api_server:app --reload --port 9000
```

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
```

The UI will be available at `http://localhost:5173`.

## Usage Guide

1.  **Generate Pad**: Go to "Pad Manager" and generate a new pad using the camera (or sample image).
2.  **Export Pad**: Click "Export Pad to QR Frames" to save the pad as a sequence of QR codes in `data/qr_frames`.
3.  **Import Pad**: On the recipient device, use "Import Pad from QR" to scan the frames and reconstruct the pad.
4.  **Secure Chat**: Use the Chat interface to encrypt messages. Copy the JSON packet and send it via any insecure channel (email, WhatsApp, etc.).
5.  **Decrypt**: Paste the received JSON packet into the Decrypt box to reveal the message.

## Security Notes

- Pads are stored in `data/pads/`. access to this directory equates to immediate compromise.
- `registry.json` tracks metadata but `data/offsets/` is the authoritative source for crash recovery.
- If a pad is exhausted or compromised, the system will reject further encryption attempts.
