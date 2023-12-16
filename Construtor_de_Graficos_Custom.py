# No exemplo abaixo vamos dar continuação à construção de gráficos personalizados. Para isso basta modificar as especificações da função plt.plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 2, 9, 7]

plt.plot(x,y, color = "yellow", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "red", markersize = 5)

# Vamos plotar também uma escala dos eixos

plt.ylim(1, 10)
plt.xlim(1, 10)

# O resto do código é o mesmo do gráfico simples

plt.xlabel('Qwert_X')
plt.ylabel('Qwert_Y')
plt.title('Qualquer Coisa que Veio na Minha Mente Exponencial')
plt.legend()

plt.show()