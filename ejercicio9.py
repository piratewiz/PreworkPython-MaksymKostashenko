"""Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros."""

def dolares_a_euros(dolares):
    return dolares * 0.85

cantidad_dolares = 100
cantidad_euros = dolares_a_euros(cantidad_dolares)
print(f"{cantidad_dolares} dólares equivalen a {cantidad_euros:.2f} euros.")
