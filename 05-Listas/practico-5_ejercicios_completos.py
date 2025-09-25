# Ejercicio 1
multip4 = list(range(4, 101, 4))
print("Ejercicio 1:", multip4)

# Ejercicio 2
gustos = ["pizza", "helado", "música", "viajar", "programar"]
print("Ejercicio 2:", gustos[-2])  # penúltimo elemento

# Ejercicio 3
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("Python")
lista_vacia.append("Listas")
print("Ejercicio 3:", lista_vacia)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Ejercicio 4:", animales)

# Ejercicio 5 (pendiente porque no pasaste el programa)
  # max(numeros) devuelve el valor más grande de la lista (en este caso 22)
  # numeros.remove(...) elimina ese valor de la lista

# Ejercicio 6
lista = list(range(10, 31, 5))
print("Ejercicio 6:", lista[:2])  # los dos primeros

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "civic"
print("Ejercicio 7:", autos)

# Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print("Ejercicio 8:", dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

   # a) agregar jugo al tercer cliente
compras[2].append("jugo")

   # b) reemplazar fideos por tallarines
compras[1][1] = "tallarines"

   # c) eliminar pan del primer cliente
compras[0].remove("pan")

print("Ejercicio 9:", compras)

# Ejercicio 10
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Ejercicio 10:", lista_anidada)
