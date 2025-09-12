#9).Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

terremoto=int(input("ingrese la magnitud del terremoto: "))
if terremoto<3:
    print("muy leve")
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