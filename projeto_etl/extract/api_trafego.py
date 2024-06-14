import requests
import os
from dotenv import load_dotenv

class apiTraffic:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv('GOOGLE_API_KEY')

    def get_traffic_data(self, origem, destino):
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={self.google_api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
