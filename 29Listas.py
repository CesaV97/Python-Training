"Listas"
#mostrar valor de lista [2,"",2.5]
lista = [1,6,5,'perro']
print (lista[1])

#cabiar valor de la lista
lista[1] = 'gato'
print(lista)

#metodo len() - meustra el valor de objetos dentro de la lista
print(len(lista))

#metodo append() - para añadir objetos al final de la lista
agregar = lista.append("rana")
print (lista)

#metodo count - numero de aparaciones del objeto
aparicion = lista.count("perro")
print (aparicion)

#metdo index () - indica la posicion de la lista en la que se encuantra el objeto
posicion = lista.index("rana")
print (posicion)

#metodo insert() - coloca la poscion y el objeto nuevo a crear
nuevo = lista.insert(2,"cadena05")
print(lista)

#meotod pop() - elmina el ultimo elemento de la lista
eliminar = lista.pop()
print (lista)

#metodo remove() - elimina el objeto especificado
remover = lista.remove("cadena05")
print (lista)

#imprimir cada elemento de la lista con for
for elem in lista: #elem toma el valor de cada valor de la lista y los numeros de 
    #la iteraciones depende a la cantidad de objetos dentro de la lista
    print(elem) # 
    
for i in range(len(lista)): # numero de iteraciones depende de la cantidad de objetos en la lista
    print(lista[i]) # imprime el valor de la lista en cada interacion cambiando cada ciclo
    



