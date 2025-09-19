from pathlib import Path
try:
    import fitz  # PyMuPDF
except Exception:
    fitz = None

class FinancialDocumentTool:
    @staticmethod
    def read_data_tool(path: str = 'data/sample.pdf'):
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        if fitz is None:
            return {"text": None, "warning": "PyMuPDF not installed; install pyMuPDF to extract text"}
        text = []
        with fitz.open(str(path)) as doc:
            for page in doc:
                text.append(page.get_text())
        joined = "\n".join(text)
        cleaned = " ".join(joined.split())
        return {"text": cleaned}
