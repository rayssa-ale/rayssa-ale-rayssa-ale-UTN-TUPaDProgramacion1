# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Agregar nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Ejercicio 1:", precios_frutas)


# Ejercicio 2
# Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Ejercicio 2:", precios_frutas)


# Ejercicio 3
# Crear lista solo con las frutas (claves)
frutas_lista = list(precios_frutas.keys())
print("Ejercicio 3:", frutas_lista)


# Ejercicio 4
# Agenda telefónica simple
agenda_telefonica = {}
for i in range(5):
    nombre = input(f"Ingrese nombre del contacto {i+1}: ")
    numero = input(f"Ingrese número de {nombre}: ")
    agenda_telefonica[nombre] = numero

# Consultar número
nombre_consulta = input("Ingrese el nombre a consultar: ")
if nombre_consulta in agenda_telefonica:
    print(f"Número de {nombre_consulta}: {agenda_telefonica[nombre_consulta]}")
else:
    print("Contacto no encontrado.")


# Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.split()

# Palabras únicas usando set
palabras_unicas = set(palabras)
print("Ejercicio 5 - Palabras únicas:", palabras_unicas)

# Contar cantidad de veces que aparece cada palabra
contador_palabras = {}
for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
print("Ejercicio 5 - Conteo de palabras:", contador_palabras)


# Ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

# Promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Ejercicio 6 - Promedio de {nombre}: {promedio:.2f}")


# Ejercicio 7
# Ejemplo de sets
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

# Aprobaron ambos
ambos = parcial1 & parcial2
print("Ejercicio 7 - Aprobaron ambos:", ambos)

# Aprobaron solo uno
solo_uno = parcial1 ^ parcial2
print("Ejercicio 7 - Aprobaron solo uno:", solo_uno)

# Aprobaron al menos uno
al_menos_uno = parcial1 | parcial2
print("Ejercicio 7 - Aprobaron al menos uno:", al_menos_uno)


# Ejercicio 8
stock_productos = {}
# Agregar productos iniciales
for i in range(3):
    producto = input(f"Ingrese nombre del producto {i+1}: ")
    cantidad = int(input(f"Ingrese cantidad de {producto}: "))
    stock_productos[producto] = cantidad

# Consultar stock
producto_consulta = input("Ingrese producto a consultar: ")
if producto_consulta in stock_productos:
    print(f"Stock de {producto_consulta}: {stock_productos[producto_consulta]}")
    agregar = int(input(f"Ingrese unidades a agregar al stock de {producto_consulta}: "))
    stock_productos[producto_consulta] += agregar
else:
    nueva_cantidad = int(input(f"Ingrese cantidad para nuevo producto {producto_consulta}: "))
    stock_productos[producto_consulta] = nueva_cantidad
print("Ejercicio 8 - Stock actualizado:", stock_productos)


# Ejercicio 9
agenda_eventos = {}
for i in range(3):
    dia = input("Ingrese día del evento (ej: Lunes): ")
    hora = input("Ingrese hora del evento (ej: 14:00): ")
    evento = input("Ingrese el nombre del evento: ")
    agenda_eventos[(dia, hora)] = evento

# Consultar actividad
dia_consulta = input("Ingrese día a consultar: ")
hora_consulta = input("Ingrese hora a consultar: ")
evento = agenda_eventos.get((dia_consulta, hora_consulta), "No hay evento")
print(f"Ejercicio 9 - Evento en {dia_consulta} a las {hora_consulta}: {evento}")


# Ejercicio 10
paises_capitales = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Ejercicio 10 - Diccionario invertido:", capitales_paises)
