from datetime import datetime, timedelta

class Candle:
    
    def __init__(self, open_price, high, low, close_price, open_time, close_time):
        self.open = open_price
        self.high = high
        self.low = low
        self.close = close_price
        self.open_time = open_time
        self.close_time = close_time

    def __str__(self):
        return f"Open: {self.open}, High: {self.high}, Low: {self.low}, Close: {self.close}"

    def body(self):
        return abs(self.close - self.open)

    def is_bullish(self):
        return self.close > self.open

    def is_bearish(self):
        return self.close < self.open

    def get_timeframe(self):
        return self.close < self.open

    def get_timeframe(self):
        time_diff = self.close_time - self.open_time
        minutes = time_diff.total_seconds() / 60
        hours = minutes / 60
        days = time_diff.days

        if days > 1:
            return f"{days}d"
        elif hours > 1:
            return f"{int(hours)}h"
        elif minutes > 1:
            return f"{int(minutes)}m"
        else:
            return "1m"
