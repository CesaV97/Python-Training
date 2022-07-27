"""
Desarrolla un programa que solicite la carga de
un numero al usuario. A continuacion, debera
pedir las notas de ese numero de alumnos y
mostrar por pantalla el numero de alumnos
aprobados y suspensos
"""

alumnos = int(input("Colocar el numero de alumnos \n"))

contador_aprobados = 0
contador_reprobados = 0
for x in range (alumnos):
    nota = float(input(f"Colocar nota para alumno: {x} \n"))
    if nota >= 5:
        contador_aprobados = contador_aprobados +  1
    else:
        contador_reprobados = contador_reprobados + 1
        
print(f"numero de alumnos aporbados {contador_aprobados} \n numero de alumnos reprobados {contador_reprobados}")
