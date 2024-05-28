"""Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
"""

def contar_palabras(oracion):
    palabras = oracion.split()
    return len(palabras)

oracion = input("Ingrese una oración: ")

cantidad_palabras = contar_palabras(oracion)
print(f"La oración ingresada tiene {cantidad_palabras} palabras.")
