"""Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros."""

def millas_a_kilometros(millas):

    return millas * 1.60934

try:
    millas = float(input("Ingrese la distancia en millas: "))
    kilometros = millas_a_kilometros(millas)
    print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros.")
except ValueError:
    print("Error: Por favor ingrese una distancia válida como número decimal.")
