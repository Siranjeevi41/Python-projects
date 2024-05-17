import requests
from config import Config

def get_bridgeit_response(query):
    headers = {
        'Authorization': f'Bearer {Config.BRIDGEIT_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {'query': query}
    response = requests.post(Config.BRIDGEIT_API_URL, json=payload, headers=headers)
    return response.json().get('response')
