#Diccionario

"Como se crea un diccionario"
#no importan los tipos de datos
#from operator import mod


dicionario = {"primera":7, "segunda":16, "tercara":"tres"} 

#recuperar el valor de un diciconario
valor01 = dicionario["primera"]
print(valor01)

#Agregar una clave al diccionario
#dicionario["crear clave"] = "asignar un valor"

#modificar un valor del diccionario
modificar = dicionario["segunda"] = [1,2,3]
print (modificar)
print (dicionario)

# funcion len() - numero de objetos dentro del diccionario

#metodos disponibles 
# clear() - elimina todos los elementos 
# get() - devolver el valor del objeto o la clave que pides
# items() - devuelve la lista, trayendo la clave con su valor
# keys() - trae todas las claves que contiene el diccionario
# values() - trae todos los valores que contienen las claves
# pop() - eliminar clave especifica 
# 