"""programacion orientada a objetos
Consiste en crear objetos que simulan entidades de la vida real
como se define una clase 
"""
class Persona:
    """
    nombre = "Pepe"
    edad = 25
    email = "pepe@gmail.com"
    """
    # los attributos se definen dentro de un constructor que en python se llama
    # __init__(self)
    
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email
    
    #Definir un metodo - significa una operacion que pueden hacer los objetos de tipo persona
    #Todos los metodos deben de llevar la palabra self en los parametros
    def saludar (self):
        print (f"soy una persona de nombre {self.nombre}")
     
     #regresar datos   
    def esMayor(self):
        if (self.edad) > 18:
            return True
        else:
            return False
#crear metodo 
    def diferencia_edad (self, edad):
        return self.edad - edad
    
#Metodo de cadena    
    def __str__(self):
        #Devuelve el los valores de los attributos del nombre, edad, email 
        return f"Personas de nombre : {self.nombre}, edad {self.edad}, email {self.email}" 
    

#nombre del objeto p1 donde colocamos el nombre de la clase
p1 = Persona("pepe",25,"pepe@gmail.com")
#print(p1.nombre)
p2 = Persona("juan", 30, "juan@gmail.com")
#print(p2.nombre) #imprime el valor de cada vaor del attributo
#p1.saludar() # p1.saludar - trae la operacion saludar de la clase Persona

#mayorEdad = p1.esMayor()
#print(mayorEdad) # -> trae el metodo esMayor de la clase Persona del attibuto p1

#Self.attributo - > (nombre, edad, email)
#Vamos a poder definir software que muestran aspectos de la vida cotidiana
#propiedades = attributos(ejemplo: email, nombre, apellido)

diferencia = p1.diferencia_edad(24) #enviamos el valor solo del parametro necesario
print(diferencia)


print(p1) # imprime los valores de los attributos del p1 
print(p2) # imprime los valores de los attributos del p2 
