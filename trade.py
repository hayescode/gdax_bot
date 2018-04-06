import sys
import time
from orders import buy_market, buy_limit, sell_limit, sell_market, order_status
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

#Hardcode trading pair
product_id = 'BTC-USD'

last_trade_time = ""
last_trade_price = ""
last_trade_amount = ""

x = "testing"

def trade():
    buy = buy_market("BTC-USD", 0.01)
    buy_order_id = buy["id"]
    """
    buy_info = order_status(buy_order_id)
    buy_price = float(buy_info["executed_value"])

    trade_time = time.strftime("%a, %d %b %Y %H:%M:%S")
    trade_price = str(buy_price * 100)
    trade_amount = buy_info["size"]

    last_trade_time = trade_time
    last_trade_price = trade_price
    last_trade_amount = str(trade_amount) """
    return buy_order_id
    
    #print(trade_time, trade_price, trade_amount)

    #time.sleep(5)


@app.route("/", methods=["POST", "GET"])
def index():
    trade_id = trade()
    buy_info = order_status(trade_id)
    buy_price = float(buy_info["executed_value"])

    trade_time = time.strftime("%a, %d %b %Y %H:%M:%S")
    trade_price = str(buy_price * 100)
    trade_amount = buy_info["size"]
    
    return render_template("index.html", time=trade_time, price=trade_price, amount=trade_amount)
    #return render_template("index.html", time=last_trade_time, price=last_trade_price, amount=last_trade_amount)


app.run()
