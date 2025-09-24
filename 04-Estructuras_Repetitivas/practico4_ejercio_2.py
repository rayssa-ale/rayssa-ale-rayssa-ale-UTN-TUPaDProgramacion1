# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene

numero=int(input("ingrese un numero: "))

contador = 0
if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10  # Dividir entre 10
        contador += 1
print("La cantidad de dígitos es:", contador)