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

import statsmodels.api as sm
import scipy.stats as stats

fig = sm.qqplot(data = vals, dist= stats.distributions.expon(scale = 1/lamb),line="45")
plt.show()

#-------mods-------martin---------

import numpy as np
#aqui ^_^
lamb = 2

n = 1000

vals = np.random.exponential(scale=1/lamb, size= n)

import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(x=vals, bin = 30)
plt.title("Histograma Distribución Exponencial")
plt.xlabel("Tiempos Entre Arribos")
plt.ylabel("Frecuencia")
plt.show()

import statsmodels.api as sm
import scipy.stats as stats

fig = sm.qqplot(data = vals, dist= stats.distributions.expon(scale = 1/lamb),line="45")
plt.show()