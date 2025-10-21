#1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos.
# Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,500,10\n")
    archivo.write("Borrador,80,25\n")


#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada linea
# la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()         
        partes = linea.split(",")  
        producto=partes[0]  
        precio=partes[1]
        cantidad=partes[2]
        print(f"Producto= {producto} | Precio= {precio} | Cantidad= {cantidad}")                 


#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("\nAgregar un nuevo producto")
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")
with open("productos.txt", "a") as archivo:  
    archivo.write(f"{nombre},{precio},{cantidad}\n")
    

###4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
###una lista llamada productos, donde cada elemento sea un diccionario con claves:
###nombre, precio, cantidad.

# Crear una lista vacía para guardar los productos
productos = []

# Abrimos el archivo en modo lectura
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()           # Quita espacios y saltos de línea
        partes = linea.split(",")       # Divide por comas: ['Lapicera', '120.5', '30']

        # Creamos un diccionario para el producto
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),     # Convertimos a número decimal
            "cantidad": int(partes[2])      # Convertimos a número entero
        }

        # Agregamos el diccionario a la lista
        productos.append(producto)

# Mostramos la lista completa de productos
print(" Lista de productos cargados:\n")
for p in productos:
    print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


###5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
###producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
###no existe, mostrar un mensaje de error.

# 1️⃣ Leer productos del archivo y cargarlos en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()               # Quita saltos de línea
        partes = linea.split(",")           # Divide los datos por coma
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(producto)

# 2️⃣ Pedir al usuario el nombre del producto a buscar
buscado = input("🔍 Ingrese el nombre del producto que desea buscar: ").strip().lower()

# 3️⃣ Variable para controlar si se encontró o no
encontrado = False

# 4️⃣ Recorrer la lista y buscar coincidencias
for p in productos:
    if p["nombre"].lower() == buscado:
        print(f"\n✅ Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break  # corta el ciclo porque ya lo encontró

# 5️⃣ Si no se encontró, mostrar mensaje
if not encontrado:
    print(f"\n❌ El producto '{buscado}' no existe en el archivo.")


###6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
###productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
###productos actualizados desde la lista.
# Lista de productos cargados previamente o modificados
productos = [
    {"nombre": "Lapicera", "precio": 120.5, "cantidad": 30},
    {"nombre": "Cuaderno", "precio": 350.0, "cantidad": 15},
    {"nombre": "Goma", "precio": 80.0, "cantidad": 50}
]

# Guardar productos actualizados en el archivo
with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("✅ Archivo 'productos.txt' actualizado correctamente.")
