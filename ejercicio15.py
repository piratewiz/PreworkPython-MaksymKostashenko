"""Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos."""

def convertir_minutos_a_horas_y_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

try:
    minutos = int(input("Ingrese el número de minutos: "))
    if minutos < 0:
        print("Error: Por favor ingrese un número de minutos positivo.")
    else:
        horas, minutos_restantes = convertir_minutos_a_horas_y_minutos(minutos)
        print(f"{minutos} minutos equivalen a {horas} horas y {minutos_restantes} minutos.")
except ValueError:
    print("Error: Por favor ingrese un número entero válido como número de minutos.")
