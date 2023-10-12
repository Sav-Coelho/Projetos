import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

    cotacao = json.loads(requisicao.text)

    print('### COTAÇÃO EM TEMPO REAL ###', datetime.datetime.now())
    print('Dolar:', cotacao['USDBRL']['bid'])
    time.sleep (3600)

