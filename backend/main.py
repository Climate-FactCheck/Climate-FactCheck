# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from .factcheck_engine import check_climate_claim
from .models import ClaimRequest, FactCheckResponse

app = FastAPI(
    title="기후변화 팩트체크 API",
    description="기후변화 관련 주장에 대한 팩트체크 서비스를 제공합니다",
    version="0.1.0"
)

@app.post("/api/factcheck", response_model=FactCheckResponse)
async def factcheck_claim(request: ClaimRequest):
    """기후변화 관련 주장에 대한 팩트체크를 수행합니다."""
    try:
        result = await check_climate_claim(request.claim, request.language)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    """API 서버 상태 확인"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
