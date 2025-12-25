from audiocraft_cli.cli import main


def test_cli_main_exists():
    # GIVEN / WHEN / THEN
    assert callable(main)
