import requests
import os

BRIDGEIT_API_KEY = os.getenv("BRIDGEIT_API_KEY")

def get_bridgeit_response(prompt, category):
    headers = {
        'Authorization': f'Bearer {BRIDGEIT_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'query': prompt,
        'category': category
    }
    response = requests.post("https://bridgeit.cisco.com/api/query", headers=headers, json=data)
    return response.json()['response']
