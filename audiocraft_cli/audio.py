import numpy as np
import soundfile as sf


def prepare_audio(wav):
    """
    Convert (channels, samples) -> (samples, channels)
    """
    return wav.T


def write_wav(path: str, wav, sample_rate: int):
    sf.write(path, wav, sample_rate)
