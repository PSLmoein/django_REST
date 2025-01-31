import requests



endpoint = 'http://localhost:8000/api/products/'

data = {
    'name': 'done by function based view 555 and no content',
    'price': 555,
}

response = requests.post(endpoint, json= data)
print(response.status_code)
print(type(response))
print(response.json())
