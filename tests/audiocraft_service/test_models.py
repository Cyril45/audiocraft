from audiocraft_service.models import validate_model_id


def test_validate_model_id_returns_string():
    # GIVEN
    model = "facebook/musicgen-small"

    # WHEN
    result = validate_model_id(model)

    # THEN
    assert result == model
