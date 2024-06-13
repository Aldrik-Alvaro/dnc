import os
from datetime import datetime
from projeto_etl.extract import api_clima, api_trafego


class projeto:
    def __init__(self):
        self.data = datetime.now()
        self.data_strftime = self.data.strftime("%d_%m_%Y")
        self.diretorio_raiz = os.getcwd()
        self.current_date = datetime.now()

    def run(self):
        print('iniciando extração')

        obj_weather = api_clima.weather()
        obj_traffic = api_trafego.traffic()


        ## EXTRACT - CLIMA ##
        cidades = ['Sao Paulo', 'Rio de Janeiro', 'Brasilia', 'Curitiba']

        weather_data_list = []
        for cidade in cidades:
            weather_data = obj_weather.get_weather_data(cidade)
            if weather_data:
                weather_data_list.append(weather_data)
        print(weather_data_list)


        ## EXTRACT - TRAFEGO ##
        rotas = [
           ('Sao Paulo', 'Rio de Janeiro'),
           ('Sao Paulo', 'Brasilia'),
           ('Rio de Janeiro', 'Curitiba')
        ]

        traffic_data_list = []
        for origem, destino in rotas:
           traffic_data = obj_traffic.get_traffic_data(origem, destino)
           if traffic_data:
               traffic_data_list.append(traffic_data)
        print(traffic_data_list)


        print("Fim da execução")
