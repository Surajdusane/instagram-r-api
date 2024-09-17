import requests

url = "http://127.0.0.1:8000/fetch-reel"
api_key = "428"
data = {
    "url": "https://www.instagram.com/reel/C_FNKvKS644/?igshid=anZib3MzNW12azkx"
}

response = requests.post(f"{url}?api_key={api_key}", json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
