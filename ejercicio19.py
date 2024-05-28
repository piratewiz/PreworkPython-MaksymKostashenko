"""Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
"""

def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

try:
    año = int(input("Ingrese un año: "))
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")
except ValueError:
    print("Error: Por favor ingrese un año válido como número entero.")
