import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

API_KEY = "ضع_مفتاحك_هنا"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current_price = float(data['data']['priceUsd'])
except requests.RequestException:
    sys.exit("Error fetching Bitcoin price")

print(f"${n * current_price:,.4f}")
