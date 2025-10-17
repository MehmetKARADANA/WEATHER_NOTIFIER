import requests

url = "http://127.0.0.1:8000/current-weather"

for i in range(1, 8):
    r = requests.get(url)
    print(f"{i}. İstek -> Status: {r.status_code}, Yanıt: {r.text}")
