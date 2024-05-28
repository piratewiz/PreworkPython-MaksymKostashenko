"""Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
"""

def determinar_dia_semana(numero):
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return dias_semana[numero - 1] if 1 <= numero <= 7 else "Número inválido"

numero = int(input("Introduce un número del 1 al 7: "))
print(f"El número {numero} corresponde al día {determinar_dia_semana(numero)}.")
