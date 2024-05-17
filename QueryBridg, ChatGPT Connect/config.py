import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CHATGPT_API_URL = os.getenv('CHATGPT_API_URL')
    CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
    BRIDGEIT_API_URL = os.getenv('BRIDGEIT_API_URL')
    BRIDGEIT_API_KEY = os.getenv('BRIDGEIT_API_KEY')
