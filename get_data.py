import config, csv
from binance.client import Client
import pandas as pd

client = Client(config.API_KEY, config.API_SECRET)

columns = [
    'open_time', 'open', 'high', 'low', 'close', 'volume',
    'close_time', 'quote_asset_volume', 'number_of_trades',
    'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
    'ignore'
]

def getData():
    running = True
    while running is True:
        input_val_crypto = input('Please enter a Crypto Abbreviation: ')
        if input_val_crypto != 'exit':

            input_val_timeval = input('Please enter a nemerical time value in days: ')
            input_val_crypto = str(input_val_crypto.upper())
            input_val_timeval = str(input_val_timeval)

            print(input_val_crypto, input_val_timeval)
            klines = client.get_historical_klines(f"{input_val_crypto}USDT", Client.KLINE_INTERVAL_1DAY, f"{input_val_timeval} day ago UTC")
            csvfile = open(f'data/{input_val_crypto}_1day_data_{input_val_timeval}day.csv', 'w', newline='')
            candlestick_writer = csv.writer(csvfile, delimiter=',')
            candlestick_writer.writerow(columns)

            for tick in klines:
                candlestick_writer.writerow(tick)
        else:
            running = False
            break

if __name__ == '__main__':
    getData()