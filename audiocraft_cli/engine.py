from audiocraft.models import MusicGen
from audiocraft_cli.models import validate_model_id


class MusicGenEngine:
    def __init__(self, model: str):
        self.model_id = validate_model_id(model)
        self.model = MusicGen.get_pretrained(self.model_id)

    def generate(self, prompt: str, duration: int):
        self.model.set_generation_params(duration=duration)
        wav = self.model.generate([prompt])[0]
        return wav
