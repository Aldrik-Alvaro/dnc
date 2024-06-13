import requests
import json
import pandas as pd
from datetime import datetime

class weather:
    def __init__(self):
        self.weather_api_key = 'weather_api_key'

    def get_weather_data(self, cidade):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={self.weather_api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None



