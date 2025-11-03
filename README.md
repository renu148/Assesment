# 🧠 AI Document Compliance Checker (FastAPI)

A lightweight API that accepts PDF or Word files, checks them against English writing guidelines using **LanguageTool**, and optionally returns corrected text.

---

## Features
- Upload PDF/DOCX for grammar & structure analysis  
- AI-based compliance report generation  
- Auto-correction & re-download  
- Ready for GPT-based upgrade  

---

## Run Locally
```bash
git clone https://github.com/<your-username>/ai_doc_assessor.git
cd ai_doc_assessor
pip install -r requirements.txt
uvicorn app:app --reload
│   └── test_api.py
└── README.md
