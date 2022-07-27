"""Practica 06
Escribir un programa que pida las tres notas de un alumno. 
si el promedio es mayor o igual a 5, mostrar un mensaje (promocionado)"""

nota01 = float(input(("Colocar valor de la nota 01: \n")))
nota02 = float(input(("Colocar valor de la nota 02: \n")))
nota03 = float(input(("Colocar valor de la nota 03: \n")))

promedio = (nota01 + nota02 + nota03)/3
if promedio >= 5:
    print("promocionado")
else:
    print("No promocionado")