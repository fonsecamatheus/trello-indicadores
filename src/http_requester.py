import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
BASE_URL = 'https://api.trello.com/1/boards'
BOARD_ID = 'jowzSGdI'

class HttpRequester:
    def __init__(self, endpoint: str) -> None:
        self.url = f"{BASE_URL}/{BOARD_ID}/{endpoint}"
        self.params = {
            'key': API_KEY,
            'token': API_TOKEN
        }

    def http_response(self) -> Dict[str, Any]:
        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ocorrido: {e}")
            return {}

class CardsApi(HttpRequester):
    def __init__(self):
        super().__init__('cards')

class ListsApi(HttpRequester):
    def __init__(self):
        super().__init__('lists')

class MembersApi(HttpRequester):
    def __init__(self):
        super().__init__('members')
