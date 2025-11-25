import requests

URL = "http://127.0.0.1:5000/doongool"
DNGL = requests.get(URL)
print(DNGL.content)

