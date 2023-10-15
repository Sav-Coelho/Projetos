
# A automatização de Twitter / X que irei criar aqui envolve a utilização da API do Twitter. Para que seja possível
# essa utilização é necessário que o usuário do código faça um cadastro no Twitter e que possua uma conta no sistema
# público da API. Ao criar a conta é necessário que seja gerados tanto as chaves do tipo 'consumer' como as de tipo toke
# Além disso é necessário que o pacote 'oauth2' já esteja instalado no seu Python via pip ou no Pycharm via settings.

import oauth2
import json
import pprint

consumer_key = 'INSIRA AQUI A CONSUMER KEY GERADA PELO TWITTER'
consumer_secret = 'INSIRA AQUI A CHAVE DE CONSUMER SECRET GERADA PELO TWITTER'

token_key = 'INSIRA AQUI A TOKEN KEY GERADA PELO TWITTER'
token_secret = 'INSIRA AQUI A CHAVE DE TOKEN SECRET GERADA PELO TWITTER'

# Após isso crie uma variável 'consumer' e uma variável 'token' por meio do 'oauth2'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

# Lembre que o consumer e o token são basicamente o login e a senha de acesso da API.
# Assim é possível unir os dois em uma variável usuário

usuario = oauth2.Client(consumer, token)

# Após criado o usuario podemos acessar o API do Twitter para realizar requisições com o request
query = input('Digite aqui o que você gostaria de pesquisar: \n')

requisicao = usuario.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query)

# O query buscado deve ser inserido após o q= da URL acima. Lembre que ele deve ser decodificado em seguida

requisicao_decod = requisicao['inserir índice da informação desejada'].decode()

# Agora podemos converter o código decodificado de json para dicionário Python

requisicao_json = json.loads(requisicao_decod)

pprint.pprint(requisicao_json['statuses'][0]['user']['screen_name'])
pprint.pprint(requisicao_json['statuses'][0]['text'])
