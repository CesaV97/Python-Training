"""
Escribir un programa que solicite la entrada de una oracion
al usuario y devuelva el numero de espacion en blanco que contiene
"""

oracion = input("Escribir oracion: \n")
espacios = oracion.count(" ")
print(f"numero de espacios en blancos es: {espacios}")