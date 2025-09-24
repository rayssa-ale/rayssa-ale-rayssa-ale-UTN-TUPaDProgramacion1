#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

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
