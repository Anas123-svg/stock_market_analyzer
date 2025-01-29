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