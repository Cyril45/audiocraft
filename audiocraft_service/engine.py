from audiocraft.models import MusicGen
from audiocraft_service.models import validate_model_id


class MusicGenEngine:
    def __init__(self, model: str):
        self.model_id = validate_model_id(model)
        print(
            f"▶ Chargement du modèle {self.model_id}… "
            "(cela peut prendre du temps au premier lancement)",
            flush=True,
        )
        self.model = MusicGen.get_pretrained(self.model_id)
        print("▶ Modèle prêt", flush=True)

    def generate(self, prompt: str, duration: int):
        self.model.set_generation_params(duration=duration)
        wav = self.model.generate([prompt])[0]
        return wav
