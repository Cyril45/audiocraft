import numpy as np
from audiocraft_cli.audio import prepare_audio


def test_prepare_audio_transposes():
    # GIVEN
    wav = np.zeros((2, 100))

    # WHEN
    result = prepare_audio(wav)

    # THEN
    assert result.shape == (100, 2)
