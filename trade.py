import sys
import time
from orders import buy_market, buy_limit, sell_limit, sell_market, order_status, account_status
from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from SQL_LOG import Log

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gdax-bot:thisismyfirstbot!!!BTC@localhost:8889/gdax-bot'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'oaieitoqhwgasd'

#Hardcode trading pair
product_id = 'BTC-USD'

def trade():
    order = buy_market("BTC-USD", 0.01)
    buy_order_id = order["id"]
    trade = order_status(buy_order_id)

    #prepare for db entry
    trade_id = trade["id"]
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
    executed_value = (float(trade["executed_value"])) * 100
    status = trade["status"]
    settled = trade["settled"]

    #enter into db
    new_record = Log(trade_id,size,product_id,side,funds,trade_type,post_only,created_at,done_at,done_reason,fill_fees,filled_size,executed_value,status,settled)
    db.session.add(new_record)
    db.session.commit()

    return buy_order_id


@app.route("/", methods=["POST", "GET"])
def index():
    trade_id = trade()

    #order info
    buy_info = order_status(trade_id)
    buy_price = float(buy_info["executed_value"])
    trade_time = time.strftime("%a, %d %b %Y %H:%M:%S")
    trade_price = str(buy_price * 100)
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


app.run()