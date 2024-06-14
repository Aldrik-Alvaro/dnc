import requests
import os
import logging
from dotenv import load_dotenv


class apiWeather:
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def get_weather_data(self, cidade):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={self.weather_api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            try:
                error_message = response.json().get('message')
                self.logger.error(f"Detalhes do erro: {error_message}")
            except Exception as e:
                self.logger.error(f"Erro ao obter detalhes do erro: {str(e)}")
            return None