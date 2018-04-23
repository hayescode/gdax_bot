import sys
import time
from orders import buy_market, buy_limit, sell_limit, sell_market, order_status, account_status
from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from SQL_LOG import record_in_db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gdax-bot:thisismyfirstbot!!!BTC@localhost:8889/gdax-bot'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'oaieitoqhwgasd'

#Hardcode trading pair
product_id = 'BTC-USD'

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        order_type = request.form["order_type"]
        amount = request.form["amount"]
        if request.form["price"]:   #if there is a price submitted (i.e. limit order), get the price
            price = request.form["price"]
        if order_type == "buy_market":
            order = buy_market(product_id, amount)
            order_id = order["id"]
            record_in_db(order_id)  #record order in db
        # if order_type == "buy_limit":
        #     order = buy_limit(product_id, amount, price)
            
        # if order_type == "sell_market":
        #     order = sell_market(product_id, amount)
        #     order_id = order["id"]
        #     record_market_in_db(order_id)  #record order in db
        # if order_type == "sell_limit":
        #     order = sell_limit(product_id, amount, price)


        buy_info = order_status(order_id)
        buy_price = float(buy_info["executed_value"])
        trade_time = time.strftime("%a, %d %b %Y %H:%M:%S")
        trade_price = format((buy_price * 100), ".2f")
        trade_amount = buy_info["size"]

        #account info
        account = account_status()
        BTC = account["balance"]
        BTC_balance = format(float(BTC), ".4f")

        fiat = buy_info["funds"]
        fiat_balance = format(float(fiat), ".2f")
        USD_balance = "$" + str(fiat_balance)

        return render_template("index.html", time=trade_time, price=trade_price, amount=trade_amount, BTC_balance=BTC_balance, USD_balance=USD_balance)
        #return render_template("index.html", time=last_trade_time, price=last_trade_price, amount=last_trade_amount)
    else:
        return render_template("index.html")


app.run()