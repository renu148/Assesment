from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_upload_docx():
    with open("sample.docx", "rb") as f:
        res = client.post("/upload/", files={"file": ("sample.docx", f, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")})
    assert res.status_code == 200
    assert "compliance_report" in res.json()
