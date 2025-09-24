# EJERCICIO 1
for i in range(0,101):
    print (i)

# EJERCICIO 2
numero=int(input("ingrese un numero: "))

contador = 0
if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10  # Dividir entre 10
        contador += 1
print("La cantidad de dígitos es:", contador)

# EJERCICIO 3
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
suma = 0
for i in range(num1 + 1, num2):
    suma += i

print("La suma de los números comprendidos entre", num1, "y", num2, "es:", suma)

# EJERCICIO 4
suma = 0
print("Ingresa números enteros para sumar. Ingresa 0 para terminar.")
while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break 
    suma += numero 
print("La suma total es:", suma)

# EJERCICIO 5 
import random
numero_secreto = random.randint(0, 9)
print("Adivina el número secreto entre 0 y 9")
intentos = 0
acertado = False
while not acertado:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    
    if intento == numero_secreto:
        acertado = True
    else:
        print(" No es el número, intenta de nuevo.")

print(" El número era", numero_secreto)
print("Te tomó", intentos, "intentos adivinarlo.")

# EJERCICIO 6
for i in range(100, -1): 
    print(i%2==0)

# EJERCICIO 7
n = int(input("Ingresa un número entero positivo: "))

suma = 0
for i in range(1, n + 1): 
    suma += i
print("La suma de los números entre 0 y", n, "es:", suma)

# EJERCICIO 8
cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cantidad} números enteros:")

for i in range(cantidad):
    num = int(input(f"Número {i+1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("--- Resultados ---")
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

# EJERCICIO 9
cantidad = 100
suma = 0
print(f"Ingrese {cantidad} números enteros:")

for i in range(cantidad):
    num = int(input(f"Número {i+1}: "))
    suma += num

media = suma / cantidad

print("--- Resultado ---")
print("La media  es:", media)

# EJERCICIO 10
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




