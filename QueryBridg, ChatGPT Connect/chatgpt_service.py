import requests
from config import Config

def get_chatgpt_response(query):
    headers = {
        'Authorization': f'Bearer {Config.CHATGPT_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'prompt': query,
        'max_tokens': 500
    }
    response = requests.post(Config.CHATGPT_API_URL, json=payload, headers=headers)
    return response.json().get('choices')[0].get('text')
