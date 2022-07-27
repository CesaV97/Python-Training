""" 
Escribir un programa que solicite dos fechas al usuario con el formato dd/mm/yyyy. 
A continuacion debe crear dos tuplas y almacenar el día, mes y años de las fechas
en dichas tuplas. por el ultimo tiene que mostrar cual de las 2 fechas es la mas reciente
"""
fecha01 = input("Colocar fecha01 con formato dd/mm/yyy: \n")
fecha02 = input("colocar fecha02 con formato dd/mm/yyyy: \n")

lista01 = fecha01.split("/") #explotamos la cadena y la hacemos una lista
lista02 = fecha02.split("/")

lista01 = tuple(lista01) # la lista la convertimos en una tupla
lista02 = tuple(lista02)

if int(lista01[2]) > int(lista02[2]):
    print ("Fecha mas reciente " + fecha01)
elif int(lista01[2]) < int(lista02[2]):
    print ("Fecha mas reciente " + fecha02)
elif int(lista01[1]) > int(lista02[1]):
    print ("Fecha mas reciente " + fecha01)
elif int(lista01[1]) < int(lista02[1]):
    print ("Fecha mas reciente " + fecha02)    
elif int(lista01[0]) > int(lista02[0]):
    print ("Fecha mas reciente " + fecha01)
elif int(lista01[0]) < int(lista02[0]):
    print ("Fecha mas reciente " + fecha02)
else:
    print("las fechas son iguales")



