
# ♻️ EcoLens: Localized Edge-AI for Waste Management

EcoLens is a privacy-focused, high-performance computer vision application designed to automate waste segregation. By leveraging a dual-stage inference pipeline, the system identifies multiple objects in real-time and provides context-aware disposal guidance based on global sustainability standards.



## 🚀 Technical Highlights
* **On-Device Inference:** Optimized for **Apple Silicon (M4)** using Metal Performance Shaders (MPS), eliminating the need for cloud-based processing.
* **Dual-Stage Pipeline:** Uses **YOLOv10** for zero-latency object detection and **Llama 3.2 Vision** for intelligent reasoning.
* **Hardware Efficiency:** Built for 16GB RAM environments using 4-bit quantization (q4_K_M) to maintain a low memory footprint.

## 🏗️ Architecture
1. **Vision Layer:** YOLOv10n scans the frame and extracts object classes.
2. **Reasoning Layer:** A local LLM (Ollama) interprets the visual data to provide sorting instructions (Recycle, Landfill, or Hazardous).
3. **Interface:** A streamlined FastAPI backend serving a responsive Streamlit dashboard.

<img width="1227" height="707" alt="image" src="https://github.com/user-attachments/assets/cbbc1c65-8543-44d9-960f-7e905540747a" />



## 🛠️ Installation & Setup

### 1. Prerequisites
* macOS (M-series chip recommended)
* [Ollama](https://ollama.com/) installed and running.
* Python 3.11+

### 2. Environment Setup
```bash
# Clone the repository
git clone https://github.com/KarimovMuhammadrasul/EcoLens.git
cd EcoLens

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

