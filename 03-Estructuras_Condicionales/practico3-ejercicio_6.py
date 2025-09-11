 #escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
 
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
