"""
Desarrolla una clase que modele el funcionamiento de una agenda
* tendra un attributo contactos, que permitira almacenar una lista
de contactos. Para contacto se tiene que guardar el nombre, telefono
y mail.
* Crear un metodo constructo que inicialice la lista de contacto 
en una lista vacia
* Crear un metodos para realizar las siguientes operaciones:
- Añadir un contacto 
- Lista de contactos 
- Buscar un contacto apartir del nombre
- Editar los datos de un contacto
* Instancia un objeto de tipo agenda  y prueba sus metodos

"""

class Agenda():
    def __init__(self):
        self.contactos = [] # definimos la lista contactos como el principal attributo

    def añadir(self):
        nombre = input("Introducir nombre del contacto: \n")
        telefono = int(input("Introducir numero de telefono: \n"))
        mail = input("Introducir correo electronico: \n")
    
        self.contactos.append({'nombre':nombre,'telefono':telefono,'mail':mail}) # introducimos los datos de la entrada en un diccionario en la lista self.contactos
        
    def enlistar(self):
        print("enlistart todos los contactos")
        
        #Ponemos la condicion para saber si hay valores en la lista
        if len(self.contactos) == 0:
            print("no hay ningun contacto")
            return
        else:
            for x in range (len(self.contactos)):
                print(self.contactos[x]['nombre']) #imprimimos el valor de la lista contactos dependiendo en el numero de iteracion
                
    def buscar(self):
        nombre = input("Introducir nombre del contacto: \n")
        
        #Recorrer la lista
        for x in range (len(self.contactos)): # X toma el valor de la lista de contactos
            print("Contacto encontrado")
            print(f"Nombre: {self.contactos[0]['nombre']}")
    