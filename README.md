# Projeto DNC

## Dependencias Necessarias:
Para executar este projeto, você precisará das seguintes ferramentas:
### Projeto ETL
- [Python 3.10 ou acima](https://www.python.org/downloads/release/python-3100/)
- [MongoDB Community Server](https://www.mongodb.com/try/download/community): Utilizado como banco de dados.
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/): IDE Python recomendada.
- [MongoCompass](https://www.mongodb.com/pt-br/products/tools/compass) (opcional): Para melhor visualização das collections no MongoDB.
### Visualização de Dados
- [Jupyter Notebook](https://jupyter.org/): Utilizado para visualização de dados plotada.
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/): Também é possível visualizar arquivos .ipynb.

## Funcionamento
https://github.com/Aldrik-Alvaro/dnc/blob/main/trafego_graficos.ipynb
Para baixar as dependências, abra o arquivo `requirements.txt` no seu IDE PyCharm e clique em `install dependencies`. Ou, execute os seguintes comandos no console:
```plaintext
pip install requests
pip install pandas
pip install pymongo
pip install python-dotenv
pip install matplotlib
```
Na raiz do projeto, no arquivo `.env`, altere as variáveis WEATHER_API_KEY e GOOGLE_API_KEY para suas respectivas chaves. Para clima, foi utilizado o serviço  [openweathermap](https://openweathermap.org/api) e para tráfego, a [Google API Directions](https://developers.google.com/maps/documentation/directions/overview?hl=pt-br)

Para iniciar o projeto, execute `main.py`. Ele iniciará o processo de ETL.

Para ver a Visualização de Dados é necessario as dependencias -
```plaintext
pip install jupyter
```
Após a instalação, abra os arquivos .ipynb e execute as células para visualizar os gráficos ou acesse os links [clima_graficos](https://www.mongodb.com/try/download/community](https://github.com/Aldrik-Alvaro/dnc/blob/main/clima_graficos.ipynb)) / [trafego_graficos](https://github.com/Aldrik-Alvaro/dnc/blob/main/trafego_graficos.ipynb)




## Estrutura do Projeto

```plaintext
projeto_etl/
    extract/
        api_clima.py
        api_trafego.py
    transform/
        transform_clima.py
        transform_trafego.py
    load/
        loadBd.py
    utils/
        util.py
    core.py
main.py
trafego_graficos.ipynb
clima_graficos.ipynb

```

## Estrutura do Projeto

- **main.py**: Script principal que inicia o projeto, chamando o `core.py`.

- **core.py**: Contém a classe principal responsável por coordenar todo o processo ETL.

- **utils/util.py**: Classe contendo funções genéricas úteis, como a função para criar um hash único para registros baseado na quantidade de colunas informadas.

- **extract/api_clima.py e api_trafego.py**: Classes para extrair dados das API's.

- **transform/transform_clima.py e transform_trafego.py**: Classes para transformar os dados das API's em um dataframe pandas para facilitar manipulações subsequentes.

- **load/loadBd.py**: Classe para carregar os dataframes de clima e tráfego para o banco de dados. Utiliza o método upsert, baseado na coluna hash gerada anteriormente, para inserir novos registros ou atualizar registros existentes.

- **graficos.ipynb**: Notebooks utilizados para plotar graficos. 




