""" Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no. """

def es_mayor_de_edad(edad):
    return edad >= 18

edad = int(input("Introduce tu edad: "))

if es_mayor_de_edad(edad):
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")
