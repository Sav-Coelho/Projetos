import numpy as np
import matplotlib.pyplot as plt

resultados = []
medias = []

for i in range(10000):

    dado1 = np.random.randint(1, 7)
    dado2 = np.random.randint(1, 7)

    amostra = (dado1 + dado2)
    resultados.append(amostra)
    medias.append(np.mean(resultados))

    print("\n O Resultado do Jogo foi: {} e {}".format(dado1, dado2))


fig = plt.figure()
ax = plt.axes()
plt.plot(medias)
plt.axhline(y=7, color='y', linestyle='-')
plt.xlabel("Número de Jogadas")
plt.ylabel("Probabilidade Média")
plt.title("A Lei dos Grandes Números no Jogo de Dados")
plt.show()

