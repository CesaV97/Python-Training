numero = int(input("introducir un numero entre 1 y 10\n"))

if numero >= 1 and numero <=10:
    nombre_fichero = "tabla-" + str(numero)+".txt"
    fichero = open(nombre_fichero,"w")
    for i in range(1,11):
        x = numero * i
        fichero.write(str(x)+"\n")
    fichero.close()
else:
    print("Numero incorrecto")