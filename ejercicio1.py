""" Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.  """

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input(12))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
