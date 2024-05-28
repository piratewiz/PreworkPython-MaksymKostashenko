"""Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
"""

def suma_pares():
    suma = 0
    for numero in range(2, 101, 2):  # Iterar por los números pares del 2 al 100
        suma += numero
    return suma

resultado = suma_pares()

print(f"La suma de todos los números pares del 1 al 100 es: {resultado}")
