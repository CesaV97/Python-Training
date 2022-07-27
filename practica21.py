"""
Desarrollar una aplicacion para la gestion de empleados de una empresa. 
la aplicacion mostrara un menu con las siguientes opciones:

1- Inicializar: Creara la base de datoas y la tabla( si no existen)
donde almacenar los empleados

2.- Insertar empleados: Pedira dni, nombre y apellidos, edad
y departamento y realizara la insercion del
empleado en la base de datos

3. Consultar: Pedira el dni del empleado y mostrara sus datos

4.- Finalu¿izar: Saldra de la aplicacion
"""

from os import curdir
from colorama import Cursor
import pymysql
#Crear funciones para cada una de la opciones 
def inicializar():
    contraseña = "Start001"
    conexion = pymysql.connect(host="localhost", user="root", passwd=contraseña)
    cursor = conexion.cursor()
    sql = "CREATE database if not exists practica21"
    cursor.execute(sql)
    sql = "USE practica21"
    cursor.execute(sql)
    sql = "CREATE table if not exists empleado (dni varchar(10), nombre varchar(255), edad smallint, departamento varchar(255))"
    cursor.execute(sql)
    
    conexion.close()
    return 1
#Funcion para insertar empleados
def insertar_empleados(dni, nombre, edad, departamento):
    contraseña = "Start001"
    conexion = pymysql.connect(host="localhost", user="root", passwd=contraseña, database="practica21")
    
    cursor = conexion.cursor()
    
    sql = "INSERT into empleado(dni, nombre, edad, departamento) value('"+dni+"','"+nombre+"',"+str(edad)+",'"+departamento+"')"
    cursor.execute(sql)
    
    conexion.commit()
    conexion.close()
    
#Funcion para consultar empleados     
def consultar_empleados(dni):
    contraseña = "Start001"
    conexion = pymysql.connect(host="localhost", user="root", passwd=contraseña, database="practica21")
    
    cursor = conexion.cursor()
    
    sql = "SELECT * from empleado where dni = '"+dni+"'"
    
    cursor.execute(sql)
    filas = cursor.fetchall()
    
    if len(filas) == 0:
        print("empleado no encontrado")
    else:
        for fila in filas:
            print(f"Empleado con dni {fila[0]} de nombre {fila[1]} y edad {fila[2]}. Trabaja en el departamento {fila[3]}")
            
    conexion.close()
    
opcion = -1
while opcion != 4:
        opcion = int(input("Introducir alguna de las opciones : \n1. Inicializar base de datos")        )
        if opcion == 1:
            resultado = inicializar()
            if resultado == 1:
                opcion = 4            
        elif opcion == 2:
                dni = input("Introduce el dni: ")
                nombre = input("introduce nombre")
                edad = int(input("Ingresar edad"))
                departamento = input("Ingresar departamento")
                insertar_empleados(dni,nombre, edad, departamento)
        elif opcion == 3:
                dni = input("Ingresar DNI \n")
                consultar_empleados(dni)
                
print("Salio del programa")
