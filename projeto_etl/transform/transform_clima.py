import pandas as pd
from datetime import datetime
from projeto_etl.utils import util

class transformWeather:
    def __init__(self):
        self.cleaned_data = []

    def clean_weather_data(self, weather_data_list):
        for raw_data in weather_data_list:
            if raw_data:
                data = {
                    'city': raw_data['name'],
                    'temperature': raw_data['main']['temp'],
                    'feels_like': raw_data['main']['feels_like'],
                    'temp_min': raw_data['main']['temp_min'],
                    'temp_max': raw_data['main']['temp_max'],
                    'pressure': raw_data['main']['pressure'],
                    'humidity': raw_data['main']['humidity'],
                    'visibility': raw_data.get('visibility', None),
                    'wind_speed': raw_data['wind']['speed'],
                    'wind_deg': raw_data['wind']['deg'],
                    'weather_main': raw_data['weather'][0]['main'],
                    'weather_description': raw_data['weather'][0]['description'],
                    'clouds_all': raw_data['clouds']['all'],
                    'dt': datetime.utcfromtimestamp(raw_data['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                    'sunrise': datetime.utcfromtimestamp(raw_data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
                    'sunset': datetime.utcfromtimestamp(raw_data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),
                    'country': raw_data['sys']['country']
                }
                data['hashId'] = util.create_hashid(f"{raw_data['name']}_{raw_data['sys']['country']}_{datetime.utcfromtimestamp(raw_data['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
                self.cleaned_data.append(data)
        return pd.DataFrame(self.cleaned_data)