#Tuplas

from operator import index
from typing import List


t = (1,2,"casa")
print (t[0])

#las tuplas no se pueden modificar
#con el metodo len podemos saber la cantidad de los elementos dentro de la tupla

#convertir una lista en una tupla utilizando el metodo - tuple()
Lista = [1,2,3]
tuplas = ("uno", "dos", "tres")
Lista = tuple(Lista) 
print(Lista)

#convertir una tupla en lista utilizando el metodo - list()
tuplas = list(tuplas)
print(tuplas)

#meotod  - count() para mostrar el numero de apariciones dentro de la tupla
contar = Lista.count(1)
print(contar)

# metodo - index() - el valor define la posicion del objeto en la tuplas
posicon =Lista.index(3)
print(posicon)