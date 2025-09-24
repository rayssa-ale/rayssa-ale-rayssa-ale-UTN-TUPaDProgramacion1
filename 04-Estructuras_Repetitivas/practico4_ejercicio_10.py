#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitar un número entero
numero = int(input("Ingresa un número entero: "))

numero_invertido = 0
if numero < 0:
    signo = -1
else:
    signo = 1
numero = abs(numero)

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
numero_invertido *= signo

print("El número invertido es:", numero_invertido)
