"""Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona."""

def calcular_imc():
    peso = float(input("Ingrese su peso en kilogramos (kg): "))
    altura = float(input("Ingrese su altura en metros (m): "))
    
    imc = peso / (altura ** 2)
    
    print(f"Su IMC es: {imc:.2f}")

calcular_imc()
