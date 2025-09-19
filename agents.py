# Minimal agent placeholders for compatibility

def financial_analyst_parse(text: str, prompt: str):
    return {"text": text}

def verifier_parse(result: dict):
    return isinstance(result, dict)
