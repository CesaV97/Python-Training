"""
desarrolla un programa que simule un traductor ingles - español. Al inciar el programa, aparecera el menu
con las siguientes opciones
1.- insertar palabra: solicitara al usuario  una palabra en ingles y su traduccion en español y la 
añadira al diccionario

2.- Traducir texto: solicitara al usuario un texto y mostrara por pantalla la traduccion del mismo.
las palabras que no es encuentren en el diccionario, las traducira como X

3.- Salir: la aplicacion finalizara
"""
opcion = 0
diccionario = {}

while opcion != "3":
    #opcion = input("seleccionar menu \n ")
    if opcion == "1":
        #print("Insertar palabra español / ingles \n")
        palabraEspañol = input("Insetart text español \n")
        palabraIngles = input("insertar texto ingles \n")
        diccionario[palabraEspañol] = palabraIngles
        opcion = input("seleccionar menu \n ")
    elif opcion == "2":
        #print("insertar palabra para traducir \n")
        texto = input("Escribir texto a traducir \n")
        texto_traducido = ""
        lista_palabras = texto.split()
        for palabra in lista_palabras:
            if palabra in diccionario:
                traduccion = diccionario[palabra]
                texto_traducido = traduccion + " "
            else:
                texto_traducido = "X" + " "
            print(texto_traducido)
        opcion = input("seleccionar menu \n ")    
    else:
        opcion = input("seleccionar menu 1, 2 o precione 3 para salir \n ")
