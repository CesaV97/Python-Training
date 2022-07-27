#Escribe un programa que pida el radio de un circulo y calcule su area, area= pi*r^2
radio = float(input("Escribir radio de un circulo: \n"))
pi = 3.1416
area = pi * pow(radio,2)
print (round(area))
print (f"el area del circulo con radio {radio} es {round(area)}")