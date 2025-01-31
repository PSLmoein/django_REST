import requests

endpoint = "http://127.0.0.1:8000/api/"

response = requests.post(endpoint, params={'qwe': 132}, json={'name':'hello world','price':250})

print(response.status_code)
print(type(response))
#print(response.json())
#print(response.text)

