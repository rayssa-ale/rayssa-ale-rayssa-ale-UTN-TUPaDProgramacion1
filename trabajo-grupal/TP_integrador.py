
# 1) Diccionario de alumnos
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# 2) Lista base de materias
materias_base = [
    ["Ciencias", 0, 0, 0],
    ["Historia", 0, 0, 0],
    ["Geografia", 0, 0, 0],
    ["Matematicas", 0, 0, 0],
    ["Fisica", 0, 0, 0]
]

# 3) Lista de notas finales de todos los alumnos
notasFinales = []


def validar_nota(mensaje):
    """Valida que la nota esté en el rango 0-10"""
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 10:
                return nota
            else:
                print(" La nota debe estar entre 0 y 10.")
        except ValueError:
            print(" Ingrese un número válido.")


def mostrar_materias(materias):
    """Muestra la tabla de materias con notas"""
    print("\nMaterias y notas:")
    print("{:<12} {:<6} {:<6} {:<6}".format("Materia", "Nota1", "Nota2", "Final"))
    for mat in materias:
        print("{:<12} {:<6} {:<6} {:<6}".format(mat[0], mat[1], mat[2], mat[3]))


# PROCESO PRINCIPAL
for legajo, nombre in alumnos.items():
    print("\n----------------------------------")
    print(f"Alumno: {nombre} (Legajo {legajo})")

    # Copiar la lista base de materias para cada alumno
    materias = [fila[:] for fila in materias_base]

    # Cargar notas por materia
    for materia in materias:
        print(f"\nIngrese las notas para la materia {materia[0]}:")

        nota1 = validar_nota("Nota 1: ")
        nota2 = validar_nota("Nota 2: ")
        promedio = (nota1 + nota2) / 2

        # Asignar valores en la tabla
        materia[1] = nota1
        materia[2] = nota2
        materia[3] = promedio

        print(f"➡ Nota Final en {materia[0]}: {promedio:.2f}")

    # Mostrar todas las materias cargadas
    mostrar_materias(materias)

    # Determinar materia con mejor nota final
    mejor_materia = max(materias, key=lambda x: x[3])
    print(f"\n Mejor materia de {nombre}: {mejor_materia[0]} con {mejor_materia[3]:.2f}")

    # Calcular promedio general del alumno
    suma_finales = sum(m[3] for m in materias)
    promedio_general = suma_finales / len(materias)
    print(f" Promedio general de {nombre}: {promedio_general:.2f}")

    # Guardar en lista de notasFinales
    notasFinales.append([nombre, promedio_general])


# Mostrar la lista completa de promedios finales
print("\n========================================")
print("PROMEDIOS GENERALES DE LOS ALUMNOS")
print("========================================")
print("{:<20} {:<6}".format("Alumno", "Promedio"))
for nf in notasFinales:
    print("{:<20} {:<6.2f}".format(nf[0], nf[1]))

# Determinar el alumno con mejor promedio
mejor_alumno = max(notasFinales, key=lambda x: x[1])
print(f"\n El mejor promedio lo obtuvo {mejor_alumno[0]} con {mejor_alumno[1]:.2f}")