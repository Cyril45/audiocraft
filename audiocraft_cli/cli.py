import argparse
from audiocraft_cli.engine import MusicGenEngine
from audiocraft_cli.audio import prepare_audio, write_wav
from audiocraft_cli.config import DEFAULT_SAMPLE_RATE, DEFAULT_DURATION, DEFAULT_MODEL


def main():
    parser = argparse.ArgumentParser(description="AudioCraft MusicGen CLI")

    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--duration", type=int, default=DEFAULT_DURATION)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    engine = MusicGenEngine(model=args.model)
    wav = engine.generate(prompt=args.prompt, duration=args.duration)

    wav = prepare_audio(wav.cpu().numpy())
    write_wav(args.output, wav, DEFAULT_SAMPLE_RATE)


if __name__ == "__main__":
    main()
