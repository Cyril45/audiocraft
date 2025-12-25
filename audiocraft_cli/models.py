def validate_model_id(model: str) -> str:
    if not model or not isinstance(model, str):
        raise ValueError("Invalid model id")
    return model
