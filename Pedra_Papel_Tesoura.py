# Aqui temos um código de um jogo simples de Pedra, Papel e Tesoura em Python


import random

def ppp():
    jogador = input("Escolha uma opção: 'pedra', 'papel'  ou 'tesoura'\n")
    computador = random.choice(['pedra', 'papel', 'tesoura'])

    if jogador == computador:
        return 'Empate!!! 🤝'

    if vitoria_ppp(jogador, computador):
        return "Você ganhou!!! ♛"

    return 'Você perdeu!'

def vitoria_ppp(voce, oponente):
    if (voce == 'papel' and oponente == 'pedra') or (voce == 'tesoura' and oponente == 'papel') or \
       (voce == 'pedra' and oponente == 'tesoura'):

        return True

print(ppp())