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
    json_data = response.json()
    symbol = json_data['Global Quote']['01. symbol']
    open_price = json_data['Global Quote']['02. open']
    highest_price = json_data['Global Quote']['03. high']
    lowest_price = json_data['Global Quote']['04. low']
    close_price = json_data['Global Quote']['05. price']

    print(symbol)
    print(open_price)
    print(highest_price)
    print(lowest_price)
    print(close_price)
    return response.json()




if __name__ == "__main__":
    get_data("TSLA")
    get_data("SNAP")
    get_data("META")

    