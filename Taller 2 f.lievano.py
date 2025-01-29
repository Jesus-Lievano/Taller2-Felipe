import numpy as np

lamb = 5

n = 1000

vals = np.random.exponential(scale=1/lamb, size= n)

import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(x=vals, bin = 30)
plt.title("Histograma Distribución Exponencial")
plt.xlabel("Tiempos Entre Arribos")
plt.ylabel("Frecuencia")
plt.show()