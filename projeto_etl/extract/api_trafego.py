import requests
import os
import logging
from dotenv import load_dotenv

class apiTraffic:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def get_traffic_data(self, origem, destino):
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={self.google_api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK':
                return data
            elif data.get('error_message') == 'The provided API key is invalid.':
                self.logger.error("Erro: Chave da API fornecida é inválida.")
                return None
            else:
                self.logger.error(f"Erro desconhecido da API: {data.get('error_message')}")
                return None
        else:
            self.logger.error(f"Erro ao chamar API: Código {response.status_code}")
            return None