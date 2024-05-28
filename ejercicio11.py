"""Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
"""

def calcular_edad(año_nacimiento):
    año_actual = 2024 
    return año_actual - año_nacimiento

año_nacimiento = int(input("Ingrese su año de nacimiento: "))
print(f"Usted tiene {calcular_edad(año_nacimiento)} años de edad.")
