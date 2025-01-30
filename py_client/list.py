import requests



endpoint = 'http://localhost:8000/api/products/'

response = requests.get(endpoint,)
print(response.status_code)
print(type(response))
print(response.json())
