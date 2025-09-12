#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
palabra= input("ingrese una palabra o frase: ")

if palabra [-1].lower() in "aeiou":
    palabra_final= palabra + "!"
    print (palabra_final)
else:
    print (palabra)