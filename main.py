import requests

params = {"lat": 40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/iss-pass.json", params)
# print(response.content)
data = response.json()
print(type(data))
print(data)

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
print(data["number"])
print(data)
