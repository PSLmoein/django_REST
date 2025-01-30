import requests



endpoint = 'http://localhost:8000/api/products/'

data = {
    'name': 'done by class based view #332',
    'price': 400,
}

response = requests.post(endpoint, json= data)
print(response.status_code)
print(type(response))
print(response.json())
