# Uma das grandes utilidades do Python é usar ele para gerar algorítmos de visualização de dados
# O código abaixo visa introduzir uma maneira simples de "plotar" dados no Python em forma gráfica
# O primeiro passo é importar a biblioteca "matplotlib"

import matplotlib.pyplot as plt

# Em seguida geramos listas com os dados coordenados que queremos plotar. Segue abaixo exemplo ilustrativo com várias linhas.

x1 = [1, 2, 3, 4, 5]
y1 = [1, 10, 22, 35, 49]

# Para plotar nossas coordenadas basta ativar a função "plot" do matplotlib

plt.plot(x1,y1, label = "Função I")

# Fazemos o mesmo para a outra linha

x2 = [1, 3, 5, 7]
y2 = [1, 6, 10, 14]

plt.plot(x2, y2, label = "Função II")

# Usamos o plot.xlabel e o plot.ylabel para dar título aos eixos. O mesmo para título

plt.xlabel('Qwert_X')
plt.ylabel('Qwert_Y')
plt.title('Qualquer Coisa que Veio na Minha Mente Exponencial')
plt.legend()

plt.show()

# _____________________________________________________________





