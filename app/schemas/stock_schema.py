from pydantic import BaseModel
from typing import Dict, List
class StockRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    api_key: str

class BollingerBands(BaseModel):
    upper_band: List[float]
    lower_band: List[float]
    sma: List[float]

class StockResponse(BaseModel):
    ticker: str
    bollinger_bands: BollingerBands
    ema: List[float]
    processed_data: List[Dict[str, float]]