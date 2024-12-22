import requests
import json
import pandas as pd
from datetime import datetime
API_KEY = "7ec5108481734c49aa4dcdd21680fc79"
BASE_URL = "https://newsapi.org/v2/everything"
params = {
    "q": "supply chain disruption OR port delays OR geopolitical conflict",
    "from": "2024-12-01",  # Start date
    "to": "2023-12-22",    # End date
    "language": "en",
    "sortBy": "relevancy",
    "apiKey": API_KEY
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    try:
        news_data = response.json()
        print(json.dumps(news_data, indent=4))
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        print("Response content:", response.text)
else:
    print(f"Error: HTTP {response.status_code}")
    print("Response content:", response.text)
