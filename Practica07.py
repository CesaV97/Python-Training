"""Practica 07
De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa
que lea dichos datos del teclado y realice los siguiente:
* Si el sueldo es inferior a 500 y su antiguedad es igual o superiro a 10 años, 
otrogarle un aumento del 20%
* si el sueldo es inferiro a 500 pero su antigüedad es menor a 10 años,
otorgarle un aumento de 5%
* si el sueldo es mayor o igual a 500 mostrar el sueldo
en pantalla sin cambios
"""
sueldoOperador = float(input("Escribir sueldo de empleado: \n"))
añosAntiguedad = float(input("Colocar años de anitguedad de operador: \n"))
    
if sueldoOperador < 500 and añosAntiguedad >= 10:
    aumento = sueldoOperador * 0.20
    suma = sueldoOperador + aumento
elif sueldoOperador < 500 and añosAntiguedad < 10:
    aumento = sueldoOperador * 0.05
    suma = sueldoOperador + aumento

print (f"Sueldo del empleado- {sueldoOperador}")
