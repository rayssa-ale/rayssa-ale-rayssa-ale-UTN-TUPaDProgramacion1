#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
print("Ingresa números enteros para sumar. Ingresa 0 para terminar.")
while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break 
    suma += numero 
print("La suma total es:", suma)