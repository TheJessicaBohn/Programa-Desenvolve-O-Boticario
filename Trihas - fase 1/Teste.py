import matplotlib.pyplot as plt

# Dados das alturas em centimetros, altura crescente
alturas = [150, 160, 165, 175, 180, 185]

# Dados dos pesos e kg
pesos = [50, 60, 65, 70, 75, 80, 85]

plt.bar(altura, pesos) # padrão do gráfico, gráfico de barras
plt.xlabel('Altura (cm)') # eixo x, ou a legenda o gráfico
plt.ylabel('Pesos (kg)') # eixo y
plt.title('Relação entre Altura e Peso') # titulo do gráfico
plt.show()
