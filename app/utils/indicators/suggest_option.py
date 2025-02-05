import numpy as np
import pandas as pd
from app.utils.indicators.rsi import calculate_rsi

def suggest_option(data: pd.DataFrame,window: int = 14):
    data = data.copy()
    numeric_prices = data.select_dtypes(include=[np.number])    
    data["SMA"] = data["close"].rolling(window=window).mean()
    try:
        data["RSI"] = calculate_rsi(data, window)["rsi"]
    except Exception as e:
        print(f"Error calculating RSI: {e}")
        return "Error in RSI calculation."


    
    latest_price = data["close"].iloc[-1]
    latest_sma = data["SMA"].iloc[-1]
    latest_rsi = data["RSI"].iloc[-1]
    
    if latest_price > latest_sma and latest_rsi > 70:
        return "Avoid Call - Stock Overbought, Risk of Reversal ⚠️"
    elif latest_price > latest_sma and latest_rsi <= 70 and latest_rsi > 50:
        return "Buy Call Option 📈"
    elif latest_price < latest_sma and latest_rsi < 30:
        return "Avoid Put - Stock Oversold, Potential Rebound ⚠️"
    elif latest_price < latest_sma and latest_rsi >= 30 and latest_rsi < 50:
        return "Moderate Buy Put Option 📉"
    return "No clear suggestion"