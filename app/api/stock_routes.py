from fastapi import APIRouter
import pandas as pd
from app.schemas.stock_request import StockRequest
from app.schemas.stock_response import StockResponse
from app.services.analyze_data import analyze_stock
router = APIRouter()

@router.post("/analyze", response_model=StockResponse)
def analyze(request: StockRequest):
    return analyze_stock(request)











