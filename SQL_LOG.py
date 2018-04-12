from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gdax-bot:thisismyfirstbot!!!BTC@localhost:8889/gdax-bot'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_id = db.Column(db.String(250))
    size = db.Column(db.String(250))
    product_id = db.Column(db.String(250))
    side = db.Column(db.String(250))
    funds = db.Column(db.Float)
    trade_type = db.Column(db.String(250)) 
    post_only = db.Column(db.String(250))
    created_at = db.Column(db.String(250))
    done_at = db.Column(db.String(250))
    done_reason = db.Column(db.String(250))
    fill_fees = db.Column(db.Float)
    filled_size = db.Column(db.Float)
    executed_value = db.Column(db.Float)
    status = db.Column(db.String(250))
    settled = db.Column(db.String(250))

    def __init__(self, trade_id, size, product_id, side, funds, trade_type, post_only, created_at, done_at, done_reason,fill_fees, filled_size, executed_value, status, settled):
        self.trade_id = trade_id
        self.size = size
        self.product_id = product_id
        self.side = side
        self.funds = funds
        self.trade_type = trade_type
        self.post_only = post_only
        self.created_at = created_at
        self.done_at = done_at
        self.done_reason = done_reason
        self.fill_fees = fill_fees
        self.filled_size = filled_size
        self.executed_value = executed_value
        self.status = status
        self.settled = settled