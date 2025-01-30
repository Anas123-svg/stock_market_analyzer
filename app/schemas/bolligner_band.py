from pydantic import BaseModel
from typing import Dict, List

class BollingerBands(BaseModel):
    upper_band: List[float]
    lower_band: List[float]
    sma: List[float]

