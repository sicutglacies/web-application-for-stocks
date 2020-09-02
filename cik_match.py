import pandas as pd


def get_ticker(ticker):
    data = pd.read_csv('stock_data.csv')
    cik = data[data['Ticker'] == ticker]['CIK'].item()
    name = data[data['Ticker'] == ticker]['Name'].item()
    exchange = data[data['Ticker'] == ticker]['Exchange'].item()

    return cik, name, exchange