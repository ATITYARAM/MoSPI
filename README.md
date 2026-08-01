# MoSPI

### Frontend
```
cd frontend
hugo server
```

### Backend
```
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
> **error**
> curl.exe -H "X-API-KEY: d67ef738b51747334c26ca8aebff8b6d" "https://microdata.gov.in/NADA/index.php/api/datasets/292/files"


