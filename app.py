from fastapi import FastAPI, UploadFile, File, HTTPException
from utils.text_extractor import extract_text
from models.compliance_checker import check_compliance, fix_text
import tempfile

app = FastAPI(title="AI Document Compliance Checker", version="1.0")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        text = extract_text(tmp_path, file.filename)
        report = check_compliance(text)
        return {"filename": file.filename, "compliance_report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/correct/")
async def correct_text(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        text = extract_text(tmp_path, file.filename)
        corrected = fix_text(text)
        return {"filename": file.filename, "corrected_text": corrected}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
