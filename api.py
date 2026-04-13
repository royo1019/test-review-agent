import requests

API_KEY = "sk-prod-abc123supersecretkey"
BASE_URL = "http://api.example.com"

def fetch_data(user_id):
    url = BASE_URL + "/users/" + user_id
    response = requests.get(url, headers={"Authorization": API_KEY})
    data = response.json()
    return data

def send_notification(user_id, message):
    url = BASE_URL + "/notify"
    response = requests.post(url, json={"user_id": user_id, "message": message}, headers={"Authorization": API_KEY})
    return response.json()
