from unittest.mock import MagicMock, patch
from audiocraft_cli.engine import MusicGenEngine


@patch("audiocraft_cli.engine.MusicGen")
def test_engine_generate_returns_audio(mock_musicgen):
    # GIVEN
    fake_model = MagicMock()
    fake_model.generate.return_value = [MagicMock()]
    mock_musicgen.get_pretrained.return_value = fake_model

    engine = MusicGenEngine("facebook/musicgen-small")

    # WHEN
    result = engine.generate("test", 1)

    # THEN
    assert result is not None
