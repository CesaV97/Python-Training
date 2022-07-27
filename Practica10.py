"""
Desarrolla un programa que solicite constantemente la carga
de un numero al usuario. el programa finalizara cuando el usuario
introduzca un 0, momento en el que se debe visualizar la suma y el 
promedio de todos los numeros introducidos
"""
suma = 0 #acumulador
numero = -1
iteracion = 0
while numero != 0:
     numero = int(input("Colocar numero \n"))
     if numero != 0:
        suma = suma + numero
        iteracion = iteracion + 1
     
promedio = round(suma / iteracion)
print(f"promedio es {promedio} suma es {suma}")