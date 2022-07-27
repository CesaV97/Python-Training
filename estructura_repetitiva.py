"""
Estructura repetitiva

"""

for a in range(10): #se agrega el valor del 0 al 9 a X
    print(f"a {a}")

for b in range(5,10): #Se agrega el valor a b en 5 e incrementa a 9
    print (f"b {b}") 

for c in range(5,10,2): # Se agregar el valor c empezando en 5 con intervalos de 0,1,2 = 3 intervalos
    print(f"c {c}")

for d in [1,4,5,7]: # el valor d toma el valor de la lista d = 1, d=4 y las iteraciones dependen a la cantidad de items en la lista
    print(f"d {d}")

for e in "cadena": # toma los valores de los caracteres y la interaciones depende al total de caracteres
    print(f"e {e}")
