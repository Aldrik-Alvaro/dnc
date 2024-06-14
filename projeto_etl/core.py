import os
from datetime import datetime
from projeto_etl.extract import api_clima, api_trafego
from projeto_etl.transform import transform_trafego, transform_clima
from projeto_etl.load import loadBd
import logging

class projeto:
    def __init__(self):
        self.data = datetime.now()
        self.data_strftime = self.data.strftime("%d_%m_%Y")
        self.diretorio_raiz = os.getcwd()
        self.current_date = datetime.now()
        self.obj_Load = loadBd.Load('dnc')
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def run(self):
        self.clima()
        self.trafego()

    def clima(self):
        # Instanciando classes de extração e transformação do clima
        obj_apiWeather = api_clima.apiWeather()
        obj_transformWeather = transform_clima.transformWeather()

        # Lendo cidades
        cidades = ['São José dos Campos', 'Rio de Janeiro', 'Brasília', 'Curitiba']
        weather_data_list = []

        # Consultando API para obter dados do clima
        logging.info('Iniciando a consulta a API de clima.')
        for cidade in cidades:
            try:
                weather_data = obj_apiWeather.get_weather_data(cidade)
                if weather_data:
                    weather_data_list.append(weather_data)
                else:
                    logging.warning(f'Sem dados retornados para a cidade: {cidade}')
            except Exception as e:
                logging.error(f'Erro ao consultar a API para a cidade {cidade}: {e}', exc_info=True)

        # Verificando se a lista de dados do clima está vazia ou é None
        if not weather_data_list:
            logging.error('Nenhum dado de clima foi coletado. Processo interrompido.')
            return

        # Transformando os dados
        try:
            logging.info('Iniciando a transformação dos dados do clima.')
            df_weather = obj_transformWeather.clean_weather_data(weather_data_list)
            logging.info('Transformação dos dados concluída.')
        except Exception as e:
            logging.error(f'Erro ao transformar os dados do clima: {e}', exc_info=True)
            return

        # Salvando os dados no banco
        try:
            logging.info('Iniciando a operação de salvar dados no banco.')
            self.obj_Load.upsert_dataframe(df_weather, 'hashId', 'weather')
            logging.info('Dados salvos no banco com sucesso.')
        except Exception as e:
            logging.error(f'Erro ao salvar os dados no banco: {e}', exc_info=True)
            return
    def trafego(self):
        # Instanciando classes de extração e transformação do tráfego
        obj_apiTraffic = api_trafego.apiTraffic()
        obj_transformTraffic = transform_trafego.transformTraffic()

        # Definindo rotas
        rotas = [
            ('São José dos Campos', 'Rio de Janeiro'),
            ('São Paulo', 'Brasília'),
            ('Rio de Janeiro', 'Curitiba')
        ]

        traffic_data_list = []

        # Consultando API para obter dados de tráfego
        logging.info('Iniciando a consulta à API de tráfego.')
        for origem, destino in rotas:
            try:
                traffic_data = obj_apiTraffic.get_traffic_data(origem, destino)
                if traffic_data:
                    traffic_data_list.append(traffic_data)
                else:
                    logging.warning(f'Sem dados retornados para a rota: {origem} -> {destino}')
            except Exception as e:
                logging.error(f'Erro ao consultar a API para a rota {origem} -> {destino}: {e}', exc_info=True)

        # Transformando os dados
        try:
            logging.info('Iniciando a transformação dos dados de tráfego.')
            df_traffic_data = obj_transformTraffic.clean_traffic_data(traffic_data_list)
            # Verificando se o df vazio
            if df_traffic_data.empty:
                logging.error('Nenhum dado de tráfego foi coletado. Processo interrompido.')
                return
            logging.info('Transformação dos dados concluída.')
        except Exception as e:
            logging.error(f'Erro ao transformar os dados de tráfego: {e}', exc_info=True)
            return

        # Salvando os dados no banco
        try:
            logging.info('Iniciando a operação de salvar dados no banco.')
            self.obj_Load.upsert_dataframe(df_traffic_data, 'hashId', 'traffic')
            logging.info('Dados salvos no banco com sucesso.')
        except Exception as e:
            logging.error(f'Erro ao salvar os dados no banco: {e}', exc_info=True)
            return
