#ejercicio 1
edad= int(input("ingrese su edad: "))

if edad > 18 :
    print ("es mayor de edad")

#ejercicio 2
nota=int(input("ingrese su nota: "))
if nota>=6:
    print ("aprobado")
else:
    print ("desaprobado")

#ejercicio 3
num=int(input("ingrese un numero par: "))
if num%2==0 :
    print("ha ingreesado un numero par")
else: 
    print ("por favor, ingrese un numero par")

#ejercicio 4
edad=int(input("ingrese su edad: "))
if edad<12:
    print("niño")
elif edad>=12 and edad<18 :
    print("adolescente")
elif edad>=18 and edad <30 :
    print("adulto/joven")
elif edad>=30 : 
    print("adulto")

#ejercicio 5
palabra= input("ingrese una contraseña entre 8 y 14 caracteres: ")
if len(palabra)>=8 and len(palabra)<=14 :
    print ("ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6
import random
from statistics import mode, median, mean

num_aleatorio= [random.randint(1,100)for i in range (10)]
moda= mode(num_aleatorio)
mediana=median(num_aleatorio)
media=mean(num_aleatorio)
print (num_aleatorio)
print (moda)
print(mediana)
print (media)

if moda==mediana==media :
    print("sin sesgo")
elif media>mediana and mediana>moda :
    print ("Sesgo positivo o a la derecha")
elif media<mediana and mediana<moda : 
    print("Sesgo negativo o a la izquierda")
else : 
    print ("fin")

#ejercicio 7
palabra= input("ingrese una palabra o frase: ")

if palabra [-1].lower() in "aeiou":
    palabra_final= palabra + "!"
    print (palabra_final)
else:
    print (palabra)

#ejercicio 8
nombre=input("ingrese su nombre: ")

print("--------------OPCIONES---------------")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion= int(input("seleccione el numero de la opcion que desee:"))
if opcion == 1:
    nombrefinal= nombre.upper()
    print (nombrefinal)
elif opcion==2:
    nombrefinal=nombre.lower()
    print (nombrefinal)
elif opcion==3:
    nombrefinal=nombre.title()
    print(nombrefinal)
else:
    print("opcion no disponible. ingrese 1,2 o 3")

#ejercicio 9 
terremoto=int(input("ingrese la magnitud del terremoto: "))
if terremoto<3:
    print("Muy leve")
elif terremoto>=3 and terremoto<4 :
    print("Leve")
elif terremoto>=4 and terremoto<5:
    print("Moderado")
elif terremoto>=5 and terremoto<6 :
    print("Fuerte")
elif terremoto>=6 and terremoto<7 :
    print("Muy fuerte")
else:
    print("Extremo")

#ejercicio 10
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print("Estación:", estacion)

