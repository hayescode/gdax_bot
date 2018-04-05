import requests
import json
from authentication import GDAXRequestAuth

#from https://cryptostag.com/basic-gdax-api-trading-with-python/

#sandbox enviorment
api_base = 'https://api-public.sandbox.gdax.com'
api_key = 'dd2efb9335217e11a6484f7885ee00f6'
api_secret = 'Ex70Sk6buuXzunbYY2LZYpwxdVkTwM26neSGMPA3UW76h11HXzjKgEaKNYzrgGAQLPsxVY6ij4GN/VTdI4kV7Q=='
passphrase = '6kbsq93uig4'

# use our request auth object
auth = GDAXRequestAuth(api_key, api_secret, passphrase)
order_url = api_base + '/orders'
order_data = {
    'type': 'market',
    'side': 'buy',
    'product_id': 'BTC-USD',
    'size': '0.01'
}
response = requests.post(order_url, data=json.dumps(order_data), auth=auth)
print(response.json())

order_id = '1a00adf6-e7f2-414c-9a71-48f56895ba99'
order_url = api_base + '/orders/' + order_id
response = requests.get(order_url, auth=auth)
print(response.json())