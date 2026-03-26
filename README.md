# 🎙️ Transcription, Diarization & Automatic Summarization (Labor Unions)

This project allows processing long-duration audio recordings (union meetings, AGMs, etc.) to automatically generate accurate transcription, speaker identification (**diarization**), and structured reports (detailed minutes and synthetic summaries).

The whole pipeline is local to guarantee **data privacy**.

## 🛠️ Technologies Used

- **Transcription & Alignment**: [WhisperX](https://github.com/m-bain/whisperx) (`large-v3` model)
- **Diarization**: [Pyannote 3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)
- **AI Summary (LLM)**: [Qwen 3.5 9B](https://ollama.com/library/qwen2.5) via **Ollama**
- **Infrastructure**: **Docker** with GPU support (NVIDIA CUDA)

## 🚀 Quick Start

### Prerequisites
1. **Docker Desktop** (with WSL2 on Windows).
2. **NVIDIA Container Toolkit** (for GPU acceleration).
3. **Ollama** installed on the host machine.

### Configuration
1. Clone the repository:
   ```bash
   git clone https://github.com/ThomasPTD/Transcription-Dialitarisation-summary.git
   cd Transcription-Dialitarisation-summary
   ```

2. Create a `.env` file in the root directory and add your Hugging Face token (required for Pyannote):
   ```env
   HF_TOKEN=your_token_here
   ```

3. Place your audio files in the `sources/` folder.

### Running with Docker
The project is fully containerized to avoid complex dependency installation issues (FFmpeg, CUDA, etc.).

```bash
docker compose up --build
```

Once started, access **Jupyter Lab** through the URL displayed in the terminal (usually `http://localhost:8888`) to run the `pipeline_transcription.ipynb` notebook.

## 📁 Project Structure

- `sources/` : Place your audio files (`.mp3`, `.m4a`, `.wav`, `.mp4`) here.
- `resultats/` : Transcriptions, detailed minutes, and summaries will be generated here.
- `pipeline_transcription.ipynb` : The core of the project (Notebook to execute).
- `Dockerfile` & `docker-compose.yml` : Linux/GPU virtual environment configuration.
- `requirements.txt` : Python dependencies list.

## 🔒 Privacy
This pipeline runs **100% locally**. No audio or text is sent to the cloud. The summary model uses Ollama to ensure data never leaves your infrastructure.

---
*Developed for the automation of administrative and union minutes reports.*
