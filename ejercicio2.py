"""Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta. """

def calcular_total_con_propina(monto_cuenta, porcentaje_propina=15):
    propina = monto_cuenta * (porcentaje_propina / 100)
    total_a_pagar = monto_cuenta + propina
    return total_a_pagar

monto_cuenta = float(input(25))

total_a_pagar = calcular_total_con_propina(monto_cuenta)

print(f"El monto total a pagar, con una propina del 15%, es: ${total_a_pagar:.2f}")
