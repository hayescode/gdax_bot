import sys
import time
from orders import buy_market, buy_limit, sell_limit, sell_market, order_status
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

#Hardcode trading pair
product_id = 'BTC-USD'

def trade():
    order = buy_market("BTC-USD", 0.01)
    buy_order_id = order["id"]
    trade = order_status(buy_order_id)
    size = trade["size"]
    product_id = trade["product_id"]
    side = trade["side"]
    funds = trade["funds"]
    trade_type = trade["type"]
    post_only = trade["post_only"]
    created_at = trade["created_at"]
    done_at = trade["done_at"]
    done_reason = trade["done_reason"]
    fill_fees = trade["fill_fees"]
    filled_size = trade["filled_size"]
    executed_value = trade["executed_value"]
    status = trade["status"]
    settled = trade["settled"]
    return buy_order_id


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