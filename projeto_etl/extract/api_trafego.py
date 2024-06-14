import requests


class apiTraffic:
    def __init__(self):
        self.google_api_key = 'google_api_key-twmUKvY5bYGDEg'

    def get_traffic_data(self, origem, destino):
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={self.google_api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
