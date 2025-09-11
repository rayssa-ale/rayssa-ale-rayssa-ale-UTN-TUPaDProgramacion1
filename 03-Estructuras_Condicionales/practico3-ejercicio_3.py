#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
num=int(input("ingrese un numero par: "))
if num%2==0 :
    print("ha ingreesado un numero par")
else: 
    print ("por favor, ingrese un numero par")