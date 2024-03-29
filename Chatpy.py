## Nesse projeto será criado um oracle classe 0 utilizando as biblioteca "wikipedia" e "wolframalpha" do Python.
## O oracle desenvolido será bastante simples, do tipo chatbot, porém com integração a bases de dados de conhecimento público
## Objetivo central do projeto é mostrar que é possível construir geradores de resposta com código Python simples


# Primeiramente importamos as seguintes bibliotecas:

import os
import wolframalpha
import wikipedia
import textwrap

# Por qual razão importamos essas bibliotecas?

# `os` nos permite acessar variáveis de ambiente, como a chave de API do Wolfram Alpha
# `wikipedia` nos permite pesquisar e acessar artigos da Wikipedia.
# `wolframalpha` nos permite pesquisar e acessar informações do Wolfram Alpha
# 'textwrap' vai nos permitir realizar a formatação do texto de linha única para paragrafação

# Devido às limitações linguísticas das bibliotecas "wolframalpha" e "wikipedia", todas as perguntas devem ser feitas em _inglês_

# Para utilizarmos a API do Wolfram é necessário que você crie uma ID no site deles antes :)

# Aqui vamos imprimir uma mensagem de boas-vindas
print("Welcome! \n")

# Iniciar um loop infinito para receber perguntas do usuário:
while True:
    # Solicitar uma pergunta ao usuário:
    text = input("Whats your question?\n")

    # Como condição de segurança do loop, vamos criar uma palavra-mestra para interromper o programa:
    if text == "Stop":
        break

    else:
        # Primariamente, as perguntas serão buscadas na Wikipedia:
        try:
            answer = wikipedia.summary(text)  # Obtém o resumo do artigo da Wikipedia
            wrapped_answer = textwrap.fill(answer, width=70)  # Realiza a formatação customizada da resposta encontrada
            print(wrapped_answer, sep="\n")  # Imprime a resposta da Wikipedia com formação

        # Se a busca na Wikipedia falhar, tenta buscar no Wolfram|Alpha

        except:
            app_id = "[INSERIR ID]"  # Aqui você irá definir a ID. Basta inserir a que você criar no seu perfil de usuário do Wolfram...
            client = wolframalpha.Client(app_id)  # Cria um cliente Wolfram Alpha com base na sua ID de acesso
            res = client.query(text)  # Envia a pergunta ao sistema do Wolfram|Alpha

            # Tenta obter o primeiro resultado da resposta da Wolfram Alpha
            try:
                answer = next(res.results).text  # Extrai o texto do primeiro resultado
                wrapped_answer = textwrap.fill(answer,
                                               width=70)  # Realiza a formatação customizada da resposta encontrada no Wolfram
                print(wrapped_answer, sep="\n")  # Imprime a resposta formatada

            # Se não houver resultados da Wolfram Alpha, imprime uma mensagem de erro uma vez que é a última camada de busca
            except StopIteration:
                answer = "I'm sorry, but I did not understand your question...."
                print(answer)










        
