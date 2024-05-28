"""Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo."""

def calcular_area_rectangulo(longitud, ancho):
    return longitud * ancho

longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

area = calcular_area_rectangulo(longitud, ancho)
print(f"El área del rectángulo es: {area}")
