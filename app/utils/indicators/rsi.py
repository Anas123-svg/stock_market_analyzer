import numpy as np
import pandas as pd

def calculate_rsi(data: pd.DataFrame, window: int = 14):
    data = data.copy()
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    data['rsi'] = 100 - (100 / (1 + rs))
    return data
