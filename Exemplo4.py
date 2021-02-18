# Vamos criar uma lista de números aleatórios dentro de um range definido.
# Para isso iremos utilizar o numpy.
import numpy as np
# Na lista iremos gerar 6 números aleatórios em um range de 0 até 60.
lista = np.random.randint(1, 60, size=6)
print(lista)
# referencia https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
