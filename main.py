import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

alphavantage_key = config['API_KEYS']['alphavantage_key']
print(alphavantage_key)

def get_data_tesla():
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey='
    r = requests.get(url)
    data = r.json()

    symbol = data['Global Quote']['01. symbol']
    price = data['Global Quote']['05. price']

    # Print the extracted values
    print(f"Symbol: {symbol}")
    print(f"Price: {price}")