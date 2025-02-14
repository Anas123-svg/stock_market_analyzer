from fastapi import APIRouter
import pandas as pd
from app.schemas.stock_request import StockRequest
from app.schemas.stock_response import StockResponse
from app.services.analyze_data import analyze_stock
router = APIRouter()

@router.post("/analyze", response_model=StockResponse)
async def analyze(request: StockRequest):
    response = await analyze_stock(request)
    return response











