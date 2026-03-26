# Utiliser une image de base avec PyTorch et CUDA installés
# L'image officielle PyTorch v2.3 avec CUDA 12.1 est un très bon choix pour WhisperX
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# Éviter les prompts bloquants lors des installations Linux
ENV DEBIAN_FRONTEND=noninteractive

# Installation des outils système (ffmpeg est crucial ici, plus besoin du patch PyAV !)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Fixer le répertoire de travail dans le conteneur
WORKDIR /app

# Installer JupyterLab pour lire et exécuter le notebook
RUN pip install --no-cache-dir jupyterlab notebook

# Installer WhisperX, Ollama, et autres dépendances du projet
RUN pip install --no-cache-dir git+https://github.com/m-bain/whisperx.git ollama pydub av

# Exposer le port pour accéder à Jupyter depuis Windows
EXPOSE 8888

# Commande de démarrage par défaut : Lancer le notebook Jupyter sans token (facilité d'accès local)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
