#!/usr/bin/env bash
set -e

echo "[+] Creating research-grade OTP project structure (in-place)"

# Top level
mkdir -p docs core frontend backend tests scripts data

touch README.md .gitignore requirements.txt

# Docs
touch docs/{protocol_spec.md,threat_model.md,security_analysis.md,entropy_analysis.md,research_notes.md}

# Core
mkdir -p core/{crypto,entropy,pad,exchange,protocol,client,api}

touch core/crypto/{__init__.py,otp.py,pad_state.py,exceptions.py}
touch core/entropy/{__init__.py,camera.py,rgb_collapse.py,thinning.py,von_neumann.py,randomness_tests.py,utils.py}
touch core/pad/{__init__.py,pad_generator.py,pad_hash.py,pad_store.py,pad_registry.py,pad_loader.py}
touch core/exchange/{__init__.py,chunking.py,qr_encode.py,qr_decode.py,markers.py,verifier.py}
touch core/protocol/{__init__.py,message.py,serializer.py,deserializer.py,validator.py,errors.py}
touch core/client/{__init__.py,state_machine.py,encryptor.py,decryptor.py,pad_manager.py,offset_store.py,crash_recovery.py}
touch core/api/{__init__.py,entropy_api.py,pad_api.py,exchange_api.py,message_api.py,state_api.py}

# Frontend
mkdir -p frontend/src/{ui,bridge,state,types}
mkdir -p frontend/tauri/src-tauri

touch frontend/{README.md,package.json,tsconfig.json}
touch frontend/src/{main.tsx,App.tsx}
touch frontend/src/ui/{EntropyCapture.tsx,PadManager.tsx,QRExchange.tsx,ChatView.tsx,StateBanner.tsx,ErrorDialog.tsx}
touch frontend/src/bridge/{entropy.ts,pad.ts,exchange.ts,message.ts,state.ts}
touch frontend/src/state/{appState.ts,reducers.ts}
touch frontend/src/types/protocol.ts

touch frontend/tauri/src-tauri/{main.rs,python_bridge.rs}
touch frontend/tauri/tauri.conf.json

# Backend
touch backend/{README.md,app.py,models.py,routes.py,storage.py,config.py}

# Tests
touch tests/{test_otp.py,test_pad_state.py,test_entropy.py,test_exchange.py,test_protocol.py,test_client_state.py,test_end_to_end.py}

# Scripts
touch scripts/{generate_pad_from_image.py,run_randomness_tests.py,simulate_attack.py,benchmark_entropy.py}

# Data
mkdir -p data/{sample_images,pads,offsets,qr_frames,logs}

echo "[✓] In-place scaffold complete."