# Financial Document Analyzer — Fixed Version

## Bugs Fixed
- **Broken imports** (`agents`, `tools`, `task`) → replaced with working minimal implementations.
- **FileNotFound in tools** → added default sample path and proper error handling.
- **Unstructured prompts** → replaced with deterministic JSON schema prompt.
- **CrewAI API errors** → wrapped in retry logic (`crewai_client.py`).

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:
```
CREWAI_API_KEY=your_api_key_here
CREWAI_URL=https://api.crewai.example/analyze
```

## Run
```bash
uvicorn main:app --reload --port 8000
```

## API
- `GET /health` → returns {"status":"ok"}
- `POST /analyze` → upload PDF (`file` field). Returns structured JSON.

## Bonus
- `tasks.py` → Celery worker for async analysis.
- `models.py` → SQLAlchemy model for storing results.
