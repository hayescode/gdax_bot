import requests
import json
from authentication import GDAXRequestAuth

#from https://cryptostag.com/basic-gdax-api-trading-with-python/

#sandbox enviorment
api_base = 'https://api-public.sandbox.gdax.com'
api_key = 'dd2efb9335217e11a6484f7885ee00f6'
api_secret = 'Ex70Sk6buuXzunbYY2LZYpwxdVkTwM26neSGMPA3UW76h11HXzjKgEaKNYzrgGAQLPsxVY6ij4GN/VTdI4kV7Q=='
passphrase = '6kbsq93uig4'

def buy_market(product_id, size):
    auth = GDAXRequestAuth(api_key, api_secret, passphrase)
    order_data = {
        'type': 'market',
        'side': 'buy',
        'product_id': product_id,
        'size': size
    }
    response = requests.post(api_base + '/orders', data=json.dumps(order_data), auth=auth)
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

def sell_market(product_id, size):
    auth = GDAXRequestAuth(api_key, api_secret, passphrase)
    order_data = {
        'type': 'market',
        'side': 'sell',
        'product_id': product_id,
        'size': size
    }
    response = requests.post(api_base + '/orders', data=json.dumps(order_data), auth=auth)
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

def buy_limit(product_id, size, price):
    auth = GDAXRequestAuth(api_key, api_secret, passphrase)
    order_data = {
        'type': 'limit',
        'side': 'buy',
        'product_id': product_id,
        'size': size,
        'post_only': True,
        'price': price
    }
    response = requests.post(api_base + '/orders', data=json.dumps(order_data), auth=auth)
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

def sell_limit(product_id, size, price):
    auth = GDAXRequestAuth(api_key, api_secret, passphrase)
    order_data = {
        'type': 'limit',
        'side': 'sell',
        'product_id': product_id,
        'size': size,
        'post_only': True,
        'price': price
    }
    response = requests.post(api_base + '/orders', data=json.dumps(order_data), auth=auth)
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

def order_status(order_id):
    auth = GDAXRequestAuth(api_key, api_secret, passphrase)
    order_url = api_base + '/orders/' + order_id
    response = requests.get(order_url, auth=auth)
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()


""" buy = buy_market("BTC-USD", 0.01)
buy_order_id = buy["id"]
buy_info = order_status(buy_order_id)
print(buy_info) """

#print(buy_market("BTC-USD", 0.01))

#{'id': 'd2290b9b-3f02-43a7-9feb-46383fca7958', 'size': '0.01000000', 'product_id': 'BTC-USD', 'side': 'buy', 'funds': '9094.6657317700000000', 'type': 'market', 'post_only': False, 'created_at': '2018-03-29T03:51:14.774247Z', 'done_at': '2018-03-29T03:51:14.784Z', 'done_reason': 'filled', 'fill_fees': '0.2292500000000000', 'filled_size': '0.01000000', 'executed_value': '91.7000000000000000', 'status': 'done', 'settled': True}
