import requests

url = "http://127.0.0.1:5000/api/generate-citation-report"
payload = {
    "counsel_name": "Sneha Desai"
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
