#Abrir un fichero para leer y escribir
                #Ruta de fichero / modo de apertura
from email import contentmanager


fichero = open("prueba.txt","r")
contenido = fichero.read()

print(contenido)