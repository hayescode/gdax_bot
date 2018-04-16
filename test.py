import requests
import json
from authentication import GDAXRequestAuth

#from https://cryptostag.com/basic-gdax-api-trading-with-python/

#sandbox enviorment
api_base = 'https://api-public.sandbox.gdax.com'
api_key = 'dd2efb9335217e11a6484f7885ee00f6'
api_secret = 'Ex70Sk6buuXzunbYY2LZYpwxdVkTwM26neSGMPA3UW76h11HXzjKgEaKNYzrgGAQLPsxVY6ij4GN/VTdI4kV7Q=='
passphrase = '6kbsq93uig4'

account_id = "fe15d8d9-3e76-44b7-83eb-e3f26330d343"

def account_status():
    auth = GDAXRequestAuth(api_key, api_secret, passphrase)
    order_url = api_base + '/accounts/' + account_id
    response = requests.get(order_url, auth=auth)
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

#{'id': 'fe15d8d9-3e76-44b7-83eb-e3f26330d343', 'currency': 'BTC', 'balance': '94.4960388400000000', 'available': '94.49603884', 'hold': '0.0000000000000000', 'profile_id': '78798596-4f63-4a81-82b7-61c149532a2a'}

print(account_status())