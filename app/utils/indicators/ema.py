import numpy as np
import pandas as pd

def calculate_ema(data: pd.DataFrame, span: int = 20):
    data = data.copy() 
    data['ema'] = data['close'].ewm(span=span, adjust=False).mean()
    ema_values = data['ema'].fillna(0).tolist()  
    return ema_values
