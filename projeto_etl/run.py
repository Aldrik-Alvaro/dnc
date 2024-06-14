import os
from datetime import datetime
from projeto_etl.extract import api_clima, api_trafego
from projeto_etl.transform import transform_trafego, transform_clima


class projeto:
    def __init__(self):
        self.data = datetime.now()
        self.data_strftime = self.data.strftime("%d_%m_%Y")
        self.diretorio_raiz = os.getcwd()
        self.current_date = datetime.now()

    def run(self):
        print('iniciando extração')

        obj_apiWeather = api_clima.apiWeather()
        obj_apiTraffic = api_trafego.apiTraffic()
        obj_transformWeather = transform_clima.transformWeather()
        obj_transformTraffic = transform_trafego.transformTraffic()

        cidades = ['Sao Paulo', 'Rio de Janeiro', 'Brasilia', 'Curitiba']
        rotas = [
            ('Sao Paulo', 'Rio de Janeiro'),
            ('Sao Paulo', 'Brasilia'),
            ('Rio de Janeiro', 'Curitiba')
        ]
        weather_data_list = []
        traffic_data_list = []

        for cidade in cidades:
            weather_data = obj_apiWeather.get_weather_data(cidade)
            if weather_data:
                weather_data_list.append(weather_data)
        print(weather_data_list)

        for origem, destino in rotas:
           traffic_data = obj_apiTraffic.get_traffic_data(origem, destino)
           if traffic_data:
               traffic_data_list.append(traffic_data)
        print(traffic_data_list)

        df_weather= obj_transformWeather.clean_weather_data(weather_data_list)
        df_traffic_data = obj_transformTraffic.clean_traffic_data(traffic_data_list)
        print(df_weather)
        print(df_traffic_data)


        print("Fim da execução")
