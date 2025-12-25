import warnings
import argparse

from audiocraft_cli.engine import MusicGenEngine
from audiocraft_cli.audio import prepare_audio, write_wav
from audiocraft_cli.config import (
    DEFAULT_SAMPLE_RATE,
    DEFAULT_DURATION,
    DEFAULT_MODEL,
)

# Supprimer uniquement le warning PyTorch connu (sans masquer les autres)
warnings.filterwarnings(
    "ignore",
    message="torch.nn.utils.weight_norm is deprecated",
    category=UserWarning,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="AudioCraft MusicGen CLI")

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Identifiant HuggingFace du modèle MusicGen",
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Description textuelle de la musique à générer",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=DEFAULT_DURATION,
        help="Durée de la musique générée (en secondes)",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Chemin du fichier WAV de sortie",
    )

    args = parser.parse_args()

    print("▶ Initialisation du moteur MusicGen…", flush=True)
    engine = MusicGenEngine(model=args.model)

    print(
        "▶ Génération audio en cours… "
        "(cela peut prendre plusieurs secondes)",
        flush=True,
    )
    wav = engine.generate(prompt=args.prompt, duration=args.duration)

    print("▶ Post-traitement audio…", flush=True)
    wav = prepare_audio(wav.cpu().numpy())

    print("▶ Écriture du fichier audio…", flush=True)
    write_wav(args.output, wav, DEFAULT_SAMPLE_RATE)

    print(f"✅ Audio généré : {args.output}", flush=True)


if __name__ == "__main__":
    main()
