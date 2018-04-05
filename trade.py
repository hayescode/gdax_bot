import sys
import time
from orders import buy_market, buy_limit, sell_limit, sell_market, order_status
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import flask_sqlalchemy



#Hardcode trading pair
product_id = 'BTC-USD'

while True:
    buy = buy_market("BTC-USD", 0.01)
    buy_order_id = buy["id"]
    buy_info = order_status(buy_order_id)
    buy_price = float(buy_info["executed_value"])
    buy_amount = buy_info["size"]

    print(time.strftime("%a, %d %b %Y %H:%M:%S"), "price:" + str(buy_price * 100), "amount:" + buy_amount)

    time.sleep(5)
