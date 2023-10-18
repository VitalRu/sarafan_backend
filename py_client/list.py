from pprint import pprint

import requests


endpoint = 'http://127.0.0.1:8000/api/products/'

get_response = requests.get(endpoint)

if get_response.headers['content-type'] == 'application/json':
    data = get_response.json()
    pprint(data)
else:
    print('Response is not valid JSON')
