from colorama import Cursor
import pymysql 

# Crear funcion para insertar datos
contraseña = "Start001"
#Crear siempre la conexion
conexion = pymysql.connect(host="localhost", user="root", passwd=contraseña, database="prueba")
def insertar_datos(campo01, campo02, conexion):        
    #Siempre debemos de crear un cursos sobre el que haremos las operaciones
    cursor = conexion.cursor()    
    sql = "INSERT into tabla1(campo1, campo2) values ("+str(campo01) + ",'"+campo02+"')" #Funcion SQL    
    cursor.execute(sql) #Cursor para ejecutar la funcion de SQL
    conexion.commit() #Estruccion necesaria para persistir los cambios    
    conexion.close() #Cerrar la conexion
    
def actualizar_datos (campo01, campo02, conexion):    
    cursor = conexion.cursor()    
    sql = "UPDATE tabla1 set campo2 = '"+campo02+"' where campo1 = "+str(campo01)    
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def eliminar_datos(campo01,conexion):
    #conexion = pymysql.connect(host="localhost", user="root", passwd="pass", database="prueba")
    Cursor = conexion.cursor()
    sql = "DELETE from tabla1 where campo1 = "+str(campo01)
    Cursor.execute(sql)
    conexion.commit()
    conexion.close()

def seleccionar_datos(conexion):
    #conexion = pymysql.connect(host="localhost", user="root", passwd="pass", database="prueba")
    Cursor = conexion.cursor()
    sql = "SELECT * from tabla1"
    Cursor.execute(sql)
    filas = Cursor.fetchall() # devuelve una lista con todos los registro de la base de datos
    
    for fila in filas:
        print(str(fila[0]) + " " + fila[1])
        
    conexion.close()

#insertar_datos(1,"Valor01", conexion)
#insertar_datos(2,"Valor02", conexion)
#insertar_datos(3,"Valor03", conexion)
#actualizar_datos(1, "Valor05", conexion)
#eliminar_datos(3,conexion)
seleccionar_datos(conexion)
