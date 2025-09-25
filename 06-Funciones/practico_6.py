# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada desde el programa principal
imprimir_hola_mundo()


# Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Solicitar nombre al usuario y mostrar saludo
nombre_usuario = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre_usuario))


# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# Ejercicio 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar radio al usuario
radio = float(input("Ingresa el radio del círculo: "))
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")


# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Solicitar segundos al usuario
segundos = int(input("Ingresa la cantidad de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos):.2f} horas.")


# Ejercicio 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar número al usuario
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir entre 0"
    return suma, resta, multiplicacion, division

# Solicitar números al usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")


# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar peso y altura
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")


# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Solicitar temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
print(f"{celsius}°C son {celsius_a_fahrenheit(celsius):.2f}°F")


# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitar tres números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
print(f"El promedio es: {calcular_promedio(num1, num2, num3):.2f}")
