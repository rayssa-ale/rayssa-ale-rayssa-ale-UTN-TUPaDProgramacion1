#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

n = int(input("Ingresa un número entero positivo: "))

suma = 0
for i in range(1, n + 1): 
    suma += i
print("La suma de los números entre 0 y", n, "es:", suma)