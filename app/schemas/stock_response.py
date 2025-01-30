from pydantic import BaseModel
from typing import Dict, List
from app.schemas.bolligner_band import BollingerBands

class StockResponse(BaseModel):
    ticker: str
    bollinger_bands: BollingerBands
    ema: List[float]
    processed_data: List[Dict[str, float]]
    


