# Mech-GPT
Acoustic Edge Intelligence for Industrial Predictive Maintenance, optimized for AMD Ryzen AI.
**Team Axiom Lab | AMD Slingshot 2026**

### Problem Statement
Unplanned downtime in Indian factories costs **₹1–5 Lakhs/hour**; Mech-GPT is a "Digital Stethoscope" that detects micro-frictions and mechanical wear **4-48 hours** before failure, running entirely on local AMD silicon.

---

## The AMD Advantage
We leverage the **AMD Ryzen™ AI (XDNA Architecture)** and the **Vitis™ AI Execution Provider** to achieve:
* **Air-Gapped Privacy:** 100% local processing; no audio or telemetry is sent to the cloud, protecting factory IP.
* **Sub-2ms Latency:** Low-latency alerts by bypassing CPU bottlenecks through the Vitis AI handshake.
* **Grid-Resilience:** Uninterrupted monitoring during internet outages, essential for the Indian industrial landscape.

---

## Technical Stack
* **Hardware:** AMD Ryzen™ AI NPU
* **AI Acceleration:** Vitis™ AI EP + ONNX Runtime
* **Models:** TinyML Autoencoders (for unsupervised anomaly detection)
* **DSP:** Librosa (Mel-Spectrogram generation)
* **Frontend:** Streamlit

---

## 📂 Project Structure
- `/models`: Quantized ONNX models optimized for XDNA.
- `/src`: Audio processing and inference logic.
- `app.py`: The "Project Drishti" inspired dashboard.
- `requirements.txt`: Project dependencies.
