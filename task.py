import os
from crewai_client import call_crewai

DEFAULT_PROMPT = """You are a document parser. Extract the following JSON object exactly:

{
  "document_type": "string|null",
  "vendor": "string|null",
  "invoice_number": "string|null",
  "invoice_date": "YYYY-MM-DD|null",
  "due_date": "YYYY-MM-DD|null",
  "currency": "string|null",
  "total_amount": "number|null",
  "line_items": [
    {
      "description": "string",
      "quantity": "number|null",
      "unit_price": "number|null",
      "total": "number|null"
    }
  ]
}

Rules:
- Use null if field is missing.
- Dates must be YYYY-MM-DD or null.
- Return ONLY JSON (no commentary).
"""

def analyze_financial_document(file_path: str, prompt: str = DEFAULT_PROMPT):
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    return call_crewai(file_bytes, os.path.basename(file_path), prompt)
