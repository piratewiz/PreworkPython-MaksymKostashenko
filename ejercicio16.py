"""Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario."""

def contar_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = len(lista) - pares
    return pares, impares

try:
    lista_numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
    pares, impares = contar_pares_impares(lista_numeros)
    print(f"En la lista ingresada hay {pares} números pares y {impares} números impares.")
except ValueError:
    print("Error: Por favor ingrese números válidos separados por espacios.")
