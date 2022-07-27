"""
cadena - 

"""
#Esto es una cadena, todo lo que este drento de las comillas
"estos es una cadena " 

# extrae el numero de caracateres que necesitas
cadena = "esto es una cadena"
caracter = cadena[0:3]
print (caracter)

#saber cantidad de un caracter que hay dentro de una cadena metodo count
cantidad = cadena.count("a")
print(cantidad)

cantidad02 ="cadena".count("a")
print(cantidad02)

#metodo index - muestra donde se encuentra el primer caracter
caracter02 = cadena.index("a")
print(caracter02)

#metodo isdigit- demuestra si son  numeros

#metodo lower() 
cadena03 = "AA".lower()
print (cadena03)

#metodo replace -   remplaza texto de la cadena
remplazo = cadena.replace("esto","esta")
print (remplazo)

#metodo split - divir la cadena en una lista, se puede asignar caracter 
#para serpar
explotar = cadena.split()
explotar_caracter = cadena.split("a")

print(explotar,explotar_caracter)

#metodo upper() - cambia el texto a mayusculas
mayuscula = cadena.upper()
print(mayuscula)

#
for caracter in cadena:
    print(caracter)

# recorrer la cadena por indice
for i in range(len(cadena)):
    print(cadena[i])