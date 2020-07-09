import requests
url="http://192.168.20.177:3001/data"
data = {
    "name": "Nico"
}
while True:
    requests.get(url, data) 