import os
import requests
from time import sleep

CREWAI_URL = os.getenv("CREWAI_URL", "https://api.crewai.example/analyze")
CREWAI_KEY = os.getenv("CREWAI_API_KEY")

def call_crewai(file_bytes: bytes, filename: str, prompt: str, timeout: int = 60, max_retries: int = 3):
    if not CREWAI_KEY:
        raise RuntimeError("CREWAI_API_KEY not set in env")
    headers = {"Authorization": f"Bearer {CREWAI_KEY}"}
    files = {"file": (filename, file_bytes, "application/pdf")}
    data = {"prompt": prompt}
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(CREWAI_URL, headers=headers, files=files, data=data, timeout=timeout)
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return {"text": resp.text}
        except requests.RequestException:
            if attempt == max_retries:
                raise
            sleep(2 ** attempt)
