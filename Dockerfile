FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV AUDIOCRAFT_CACHE_DIR=/app/cache
ENV TZ=Etc/UTC

WORKDIR /app

# Dépendances système (FFmpeg + headers DEV)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-dev \
    python3-pip \
    ffmpeg \
    git \
    build-essential \
    pkg-config \
    libsndfile1-dev \
    libffi-dev \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavutil-dev \
    libavfilter-dev \
    libswscale-dev \
    libswresample-dev \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Python 3.10 par défaut
RUN ln -sf /usr/bin/python3.10 /usr/bin/python

# Outils pip
RUN python -m pip install --upgrade pip setuptools wheel

# Copier le repo local dans l’image
COPY . .

# Installer les deps (av==12.3.0 désormais)
RUN pip install --no-binary=pesq -r requirements.txt

# Installer AudioCraft
RUN pip install -e .

ENTRYPOINT ["python", "-m", "audiocraft_cli.cli"]
