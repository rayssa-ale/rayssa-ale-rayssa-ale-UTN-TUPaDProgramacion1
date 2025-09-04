#ejercicio 1
print("hola mundo")
#ejercicio 2
nombre=input("escribe tu nombre: ")
print(f"hola {nombre}")

#ejercicio 3
nombre=input("ingresa tu nombre: ")
apellido=input("ingresa tu apellido: ")
edad=input("ingresa tu edad: ")
residencia=input("ingresa tu residencia: ")
print(f"hola soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}. ")

#ejercicio 4
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es: {area} y El perímetro del círculo es: {perimetro}")

#ejercicio 5
seg=float(input("ingrese la cantidad de segundos: "))
horas=seg/3600
print(f"{seg} segundos, equivale a {horas} horas")

#ejercicio 6
numero = int(input("Ingrese un número: "))
print(f"{numero} x 1 = ", numero*1)
print(f"{numero} x 2 = ", numero*2)
print(f"{numero} x 3 = ", numero*3)
print(f"{numero} x 4 = ", numero*4)
print(f"{numero} x 5 = ", numero*5)
print(f"{numero} x 6 = ", numero*6)
print(f"{numero} x 7 = ", numero*7)
print(f"{numero} x 8 = ", numero*8)
print(f"{numero} x 9 = ", numero*9)
print(f"{numero} x 10 = ", numero*10)

#ejercicio 7
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese un numero: "))
s=num1+num2
r=num1-num2
m=num1*num2
d=num1/num2
print (num1,"+",num2,"=",s)
print (num1,"-",num2,"=",r)
print (num1,"x",num2,"=",m)
print (num1,"/",num2,"=",d)

#ejercicio 8
peso=(float(input("ingrese su peso: ")))
alt=(float(input("ingrese su altura: ")))
imc=peso/alt**2
print("tu indice de masa corporal es: ",imc)

#ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
f = (9/5) * celsius + 32
print("La temperatura en Fahrenheit es:", f)

#ejercicio 10
n1=float(input("ingrese un numero: "))
n2=float(input("ingrese un numero: "))
n3=float(input("ingrese un numero: "))
promedio=(n1+n2+n3)/3
print ("el promedio es: ",promedio)

