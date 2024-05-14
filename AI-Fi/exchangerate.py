import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
