import ccxt
from datetime import datetime, timedelta

def download_data(exchange_name, symbol, timeframe, start_date, end_date):
    exchange = getattr(ccxt, exchange_name)()
    start_timestamp = datetime.timestamp(datetime.strptime(start_date, '%Y-%m-%d'))
    end_timestamp = datetime.timestamp(datetime.strptime(end_date, '%Y-%m-%d'))
    # one_year_ago = datetime.now() - timedelta(days=365)
    # if start_timestamp < datetime.timestamp(one_year_ago):
    #     start_timestamp = datetime.timestamp(one_year_ago)
    # if end_timestamp < datetime.timestamp(one_year_ago):
    #     end_timestamp = datetime.timestamp(one_year_ago)
    data = exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, since=start_timestamp, until=end_timestamp)
    orders = exchange.fetch_orders(symbol=symbol)
    return data, orders
