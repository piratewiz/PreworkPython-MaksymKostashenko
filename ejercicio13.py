"""Escribe un programa que determine si un número ingresado por el usuario es primo
o no."""

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

try:
    numero = int(input("Introduce un número entero positivo mayor que 1: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
except ValueError:
    print("Error: Por favor introduce un número entero válido.")
