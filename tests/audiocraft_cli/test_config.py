from audiocraft_cli.config import DEFAULT_SAMPLE_RATE


def test_default_sample_rate_is_positive():
    # GIVEN / WHEN / THEN
    assert DEFAULT_SAMPLE_RATE > 0
