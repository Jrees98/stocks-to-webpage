import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
alphavantage_key = config['API_KEYS']['alphavantage_key']

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"

def get_data(ticker):
    stock_ticker = ticker
    stock_params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock_ticker,
        "apikey": alphavantage_key
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    print(response.json())

get_data("TSLA")

def get_data_tesla():
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey=' + alphavantage_key
    r = requests.get(url)
    data = r.json()

    symbol = data['Global Quote']['01. symbol']
    price = data['Global Quote']['05. price']

    # Print the extracted values
    print(f"Symbol: {symbol}")
    print(f"Price: {price}")

