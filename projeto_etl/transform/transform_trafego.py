import pandas as pd
from datetime import datetime
from projeto_etl.utils import util

class transformTraffic:
    def __init__(self):
        self.cleaned_data = []

    def clean_traffic_data(self, traffic_data_list):
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
                data['hashId'] = util.create_hashid(f"{leg['start_location']['lat']}_{leg['start_location']['lng']}_{leg['end_location']['lat']}_{leg['end_location']['lng']}")
                self.cleaned_data.append(data)
        return pd.DataFrame(self.cleaned_data)
