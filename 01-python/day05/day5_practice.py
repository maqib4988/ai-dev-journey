import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

print(response.status_code)
print(response.headers["Content-Type"])

data = response.json()
print(type(data))
print(data["rates"]["PKR"])

if response.status_code == 200:
    print("Success:", data["date"])
else:
    print("Request failed:", response.status_code)


# GET with query parameters
params = {"name": "Islamabad", "format": "json"}
response2 = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search", params=params
)
print(response2.url)
print(response2.json())

post_response = requests.post(
    "https://httpbin.org/post", json={"name": "Aaqib", "role": "AI Developer"}
)
print(post_response.json())

# Handling errors properly
try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
    response.raise_for_status()  # raises an exception if status is 4xx or 5xx
    data = response.json()
    print("Got data:", data["date"])
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
