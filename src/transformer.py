import json
import pandas as pd
from config import url
from api_fetcher import fetch_api_data
from logging_config import logging_configuration

def transform_data(api_data):
    return pd.json_normalize(api_data)

if __name__ == "__main__":
    data = fetch_api_data(url)
    df = transform_data(data)
    # print(df.head())
    print(data[0])
    print(type(data))
    print(len(data))
    print(df.head())
    print(df.columns.tolist())
    print(df.info())