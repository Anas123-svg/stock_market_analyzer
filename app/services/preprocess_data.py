import pandas as pd

def preprocess_data(data: pd.DataFrame):
    data['timestamp'] = pd.to_datetime(data['t'], unit='ms')
    data.rename(columns={
        "o": "open",
        "h": "high",
        "l": "low",
        "c": "close",
        "v": "volume",
    }, inplace=True)
    data.set_index('timestamp', inplace=True)
    return data[["open", "high", "low", "close", "volume"]]
