## Nesse projeto será criado um oracle classe 0 utilizando as biblioteca "wikipedia" e "wolframalpha" do Python.
## O oracle desenvolido será bastante simples, do tipo chatbot, porém com integração a bases de dados de conhecimento público
## Objetivo central do projeto é mostrar que é possível construir geradores de resposta com código Python simples

## Bibliotecas a serem importadas

import os
import wolframalpha
import wikipedia

## Mensagem de abertura
print("Welcome! 😁\n")

## Criação de loop para input de questões e respostas ao chatbot oracle
while True:
    text = input("Whats your question?\n")
    if text == "Stop":
        break
    else:
        try:

            answer = wikipedia.summary(text)
            print(answer)

        except:
            app_id = "" ## É necessário aqui inserir sua ID do Wolfram. Óbvio que eu não coloquei a minha :)
            client = wolframalpha.Client(app_id)
            res = client.query(text)

            try:
                answer = next(res.results).text
            except StopIteration:
                answer = "I'm sorry, but I did not understand your question...."

            print(answer)









        
