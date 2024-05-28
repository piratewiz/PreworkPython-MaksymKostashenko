"""Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%."""

def precio_final_con_descuento(precio):
    descuento = precio * 0.20
    precio_final = precio - descuento
    return precio_final

try:
    precio_original = float(input("Ingrese el precio del artículo: "))
    precio_final = precio_final_con_descuento(precio_original)
    print(f"El precio final después del descuento del 20% es: {precio_final:.2f}")
except ValueError:
    print("Error: Por favor ingrese un precio válido como número decimal.")
