import requests

endpoint = 'https://httpbin.org/anything'

response = requests.get(endpoint)
response = response.json()
print(response)