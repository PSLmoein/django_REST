import requests

endpoint = 'http://localhost:8000/api/products/2/'


response = requests.get(endpoint)
print(response.status_code)
print(type(response))
print(response.json())
