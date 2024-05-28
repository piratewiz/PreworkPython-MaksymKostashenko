"""Crea un programa que sume todos los números en una lista ingresada por el
usuario."""

def sumar_lista(lista):
    suma = sum(lista)
    return suma

try:
    lista_numeros = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))
    suma_total = sumar_lista(lista_numeros)
    print(f"La suma de los números en la lista es: {suma_total}")
except ValueError:
    print("Error: Por favor ingrese números válidos separados por espacios.")
