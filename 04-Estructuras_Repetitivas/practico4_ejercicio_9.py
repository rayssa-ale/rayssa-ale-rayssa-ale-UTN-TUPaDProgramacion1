#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# Definir cuántos números se van a ingresar (puedes cambiar 100 por un número menor para probar)
cantidad = 100
suma = 0
print(f"Ingrese {cantidad} números enteros:")

for i in range(cantidad):
    num = int(input(f"Número {i+1}: "))
    suma += num

media = suma / cantidad

print("--- Resultado ---")
print("La media  es:", media)
