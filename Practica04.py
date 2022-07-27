#Escribe un programa  que pida al usuario los grados cenitgrados que quiere convertir y muestre por pantalla la equivalencia con grados kelvin y grados farenheit 
#°K = 273 + °C
#°F = 1.8 * °C + 32

centigrados = int(input("Escribir grados centigrados actuales:\n"))
K = 273 + centigrados
F = (1.8 * centigrados)+32
print (f"grados Kelvin: {K} grados Farenheit: {F}")
