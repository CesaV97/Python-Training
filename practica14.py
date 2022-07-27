"""
Practica 14 
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa
debe preguntar el articulo y su precio y añadir el par al diccionario, hasta que el usuario decida
terminar (pulse la tecla f). despues se debe mostrar por pantalla la lista de la comprar y el
coste total, con el siguiente formato:
"""
articulo = ""
diccionario = {}
suma = 0
while articulo != "f":
    articulo = input("Escribir articulo o letra f para salir \n")
    if articulo != "f":
        precio = int(input(f"Escribir precio del articulo {articulo}  \n"))    
        diccionario[articulo] = precio
        suma = suma + precio    

for x in diccionario:
    precio = diccionario[x]
    print (f"{x}  :   {precio}")


print (f"costo total: {suma}")