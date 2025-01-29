import numpy as np
import pandas as pd

def calculate_bollinger_bands(prices: pd.DataFrame, window=10):
    numeric_prices = prices.select_dtypes(include=[np.number])
    
    sma = numeric_prices.rolling(window=window).mean()
    std = numeric_prices.rolling(window=window).std()
    
    upper_band = sma + (2 * std)
    lower_band = sma - (2 * std)
    
    return {
        "upper_band": upper_band.iloc[:, 0].fillna(0).tolist(),
        "lower_band": lower_band.iloc[:, 0].fillna(0).tolist(),
        "sma": sma.iloc[:, 0].fillna(0).tolist()

    }


def calculate_ema(data: pd.DataFrame, span: int = 20):
    data = data.copy() 
    data['ema'] = data['close'].ewm(span=span, adjust=False).mean()
    ema_values = data['ema'].fillna(0).tolist()  
    return ema_values



def calculate_rsi(data: pd.DataFrame, window: int = 14):
    data = data.copy()
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    data['rsi'] = 100 - (100 / (1 + rs))
    return data
