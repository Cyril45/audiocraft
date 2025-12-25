import os
import tempfile
from typing import Dict

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel

from audiocraft.models import MusicGen
from audiocraft_service.audio import prepare_audio, write_wav
from audiocraft_service.models import validate_model_id
from audiocraft_service.config import DEFAULT_SAMPLE_RATE

app = FastAPI(title="AudioCraft MusicGen API")

# Cache des modèles chargés en mémoire
_MODEL_CACHE: Dict[str, MusicGen] = {}


class GenerateRequest(BaseModel):
    model: str
    prompt: str
    duration: int = 30


def get_model(model_id: str) -> MusicGen:
    model_id = validate_model_id(model_id)

    if model_id not in _MODEL_CACHE:
        print(f"▶ Chargement du modèle {model_id}…", flush=True)
        model = MusicGen.get_pretrained(model_id)
        _MODEL_CACHE[model_id] = model
        print("▶ Modèle prêt", flush=True)

    return _MODEL_CACHE[model_id]


@app.get("/", response_class=HTMLResponse)
def index():
    with open("audiocraft_service/web/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        model = get_model(req.model)

        model.set_generation_params(duration=req.duration)
        wav = model.generate([req.prompt])[0]

        wav = prepare_audio(wav.cpu().numpy())

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            output_path = tmp.name

        write_wav(output_path, wav, DEFAULT_SAMPLE_RATE)

        return FileResponse(
            output_path,
            media_type="audio/wav",
            filename="musicgen.wav",
            background=lambda: os.remove(output_path),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
