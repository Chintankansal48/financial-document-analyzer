import os, uuid, tempfile
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from task import analyze_financial_document

load_dotenv()
app = FastAPI(title="Financial Document Analyzer - Fixed")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    tmp_path = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}_{file.filename}")
    with open(tmp_path, "wb") as f:
        f.write(contents)
    try:
        result = analyze_financial_document(tmp_path)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return JSONResponse(content=result)
