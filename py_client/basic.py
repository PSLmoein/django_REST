import requests

endpoint = "http://127.0.0.1:8000/api/"

response = requests.get(endpoint, params={'qwe': 132}, json={'query':'hello world'})

print(response.status_code)

