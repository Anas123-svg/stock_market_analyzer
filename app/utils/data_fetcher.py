import requests
import httpx
import pandas as pd

async def fetch_stock_data(ticker: str, start_date: str, end_date: str, api_key: str):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}"
    params = {
        "adjusted": "true",
        "sort": "asc",
        "apiKey": api_key,
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "results" in data:
            return pd.DataFrame(data["results"])
        else:
            raise ValueError("No results found in the API response.")
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}, Error: {response.text}")
