import pandas as pd
from app.utils.indicators import calculate_bollinger_bands


def predict_next_session(ticker):
    return {"ticker": ticker, "predicted_price": 150.25}