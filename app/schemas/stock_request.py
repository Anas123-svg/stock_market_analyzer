from pydantic import BaseModel
from typing import Dict, List

class StockRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    api_key: str

