import pandas as pd
from app.schemas.stock_schema import StockRequest, StockResponse,BollingerBands
from app.services.preprocess_data import preprocess_data
from app.utils.data_fetcher import fetch_stock_data
from app.utils.indicators.bollinger_bands import calculate_bollinger_bands
from app.utils.indicators.ema import calculate_ema
from app.utils.indicators.rsi import calculate_rsi


def analyze_stock(request: StockRequest):
    try:
        raw_data = fetch_stock_data(
            ticker=request.ticker,
            start_date=request.start_date,
            end_date=request.end_date,
            api_key=request.api_key
        )
        print(raw_data)
        
        processed_data = preprocess_data(raw_data)
        print("processed_data")
        print(processed_data)
        bollinger_bands = {}
        try:
            bollinger_bands = calculate_bollinger_bands(processed_data)
            print("bollinger_bands")
            print(bollinger_bands)
        except Exception as e:
            print(f"bollinger Error: {e}")
            
        try:
            ema = calculate_ema(processed_data, span=20)
            print("ema")
            print(ema)
        except Exception as e:
            print(f"ema Error: {e}")

        rsi_data = calculate_rsi(processed_data)
        print("RSI")
        print(rsi_data)

        response = StockResponse(
            ticker=request.ticker,
            bollinger_bands=BollingerBands(
                upper_band=bollinger_bands.get('upper_band', []),
                lower_band=bollinger_bands.get('lower_band', []),  
                sma=bollinger_bands.get('sma', [])  
            ),
            ema=ema.tolist() if isinstance(ema, pd.Series) else ema,  
            rsi=rsi_data['rsi'].tolist(),
            processed_data=processed_data.to_dict(orient="records") 
        )

        return response

    except Exception as e:
        print(f"Error: {e}")
        return StockResponse(
            ticker=request.ticker,
            bollinger_bands=BollingerBands(upper_band=[], lower_band=[], sma=[]),
            ema=[],
            rsi=[],
            processed_data=[]
        )
