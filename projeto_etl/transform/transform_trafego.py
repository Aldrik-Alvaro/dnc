import requests
import json
import pandas as pd
from datetime import datetime


class transformTraffic:
    def __init__(self):
        print("Iniciando limpeza trafego")

    def clean_traffic_data(self, traffic_data_list):
        cleaned_data = []
        for raw_data in traffic_data_list:
            if raw_data and raw_data['status'] == 'OK':
                leg = raw_data['routes'][0]['legs'][0]
                data = {
                    'start_address': leg['start_address'],
                    'end_address': leg['end_address'],
                    'distance_text': leg['distance']['text'],
                    'distance_value': leg['distance']['value'],
                    'duration_text': leg['duration']['text'],
                    'duration_value': leg['duration']['value'],
                    'start_location_lat': leg['start_location']['lat'],
                    'start_location_lng': leg['start_location']['lng'],
                    'end_location_lat': leg['end_location']['lat'],
                    'end_location_lng': leg['end_location']['lng'],
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                cleaned_data.append(data)

        return pd.DataFrame(cleaned_data)
