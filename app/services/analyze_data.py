import pandas as pd
from app.services.preprocess_data import preprocess_data
from app.schemas.stock_request import StockRequest
from app.schemas.stock_response import StockResponse
from app.schemas.bolligner_band import BollingerBands
from app.utils.data_fetcher import fetch_stock_data
from app.utils.indicators.bollinger_bands import calculate_bollinger_bands
from app.utils.indicators.ema import calculate_ema
from app.utils.indicators.rsi import calculate_rsi
from app.utils.indicators.suggest_option import suggest_option

def handle_nan(data):
    if isinstance(data, list):
        return [0 if math.isnan(x) else x for x in data]
    elif isinstance(data, pd.Series):
        return data.fillna(0).tolist()
    elif isinstance(data, dict):
        return {key: (0 if math.isnan(value) else value) for key, value in data.items()}
    return 0 if math.isnan(data) else data

async def analyze_stock(request: StockRequest):
    try:
        raw_data = await fetch_stock_data(
            ticker=request.ticker,
            start_date=request.start_date,
            end_date=request.end_date,
            api_key=request.api_key
        )
        print(raw_data)
        
        processed_data =preprocess_data(raw_data)
        print("processed_data")
        print(processed_data)
        bollinger_bands = {}
        try:
            bollinger_bands =calculate_bollinger_bands(processed_data)
            print("bollinger_bands")
            print(bollinger_bands)
        except Exception as e:
            print(f"bollinger Error: {e}")
            
        try:
            ema =calculate_ema(processed_data, span=20)
            print("ema")
            print(ema)
        except Exception as e:
            print(f"ema Error: {e}")
            
            
        try:
            rsi_data =calculate_rsi(processed_data)
            print("RSI")
            print(f"rsi_data {rsi_data}" )
        except Exception as e:
            print(f"rsi Error: {e}")
        
        try:
            option_suggestion = suggest_option(processed_data)
            print(f"option_suggestion {option_suggestion}")
        except Exception as e:
            print(f"option_suggestion Error: {e}")
        
        
        rsi_data['rsi'] = handle_nan(rsi_data['rsi'])

        response = StockResponse(
            ticker=request.ticker,
            bollinger_bands=BollingerBands(
                upper_band=bollinger_bands.get('upper_band', []),
                lower_band=bollinger_bands.get('lower_band', []),  
                sma=bollinger_bands.get('sma', [])  
            ),
            ema=ema.tolist() if isinstance(ema, pd.Series) else ema,  
            rsi=rsi_data['rsi'],
            processed_data=processed_data.to_dict(orient="records"),
            option_suggestion=option_suggestion
        )

        return response

    except Exception as e:
        print(f"Error endd: {e}")
        return StockResponse(
            ticker=request.ticker,
            bollinger_bands=BollingerBands(upper_band=[], lower_band=[], sma=[]),
            ema=[],
            rsi=[],
            processed_data=[],
            option_suggestion="Error in data processing"
        )
