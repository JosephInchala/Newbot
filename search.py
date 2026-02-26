import requests

API_KEY = "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"
URL = "https://api.tavily.com/search"

response = requests.post(URL, json={
    "query": "moltbook.com",
    "api_key": API_KEY
})

print(response.json())
