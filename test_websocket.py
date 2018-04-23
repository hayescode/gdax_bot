from websocket import WebSocketApp
from json import dumps, loads
import time

URL = "wss://ws-feed.gdax.com"

class WebSocket():
    def __init__(self):
        self.best_bid = 0
        self.best_ask = 0
        self.price = 0

    def best_bid():
        return self.best_bid

    def on_message(_, message):
        mess = loads(message)
        self.best_bid = mess['best_bid']
        self.best_ask = mess['best_ask']
        self.price = mess['price']

    def on_open(socket):
        params = {
            "type": "subscribe",
            "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
        }
        socket.send(dumps(params))

    def main():
        ws = WebSocketApp(URL, on_open=on_open, on_message=on_message)
        ws.run_forever()


if __name__ == '__main__':
    main()