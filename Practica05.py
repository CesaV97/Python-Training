#Calculadora, desarrolla una calculadora de enteros. El programa debera pedir los 2 operandos al usuario y realizas la soperaciones basicas: suma, resta, multiplicacion y divicion 
#Controlar las exepciones que se pueden producir

from audioop import mul
from pdb import Restart


try:
    operador01 = float(input("Agregar operador 01: \n"))
    operador02 = float(input("Agregar operador 02: \n"))
except:
    print("caracter incorrecto, escribe caracteres correctos")
    operador01 = float(input("Agregar operador 01: \n"))
    operador02 = float(input("Agregar operador 02: \n"))
try:    
    suma = operador01 + operador02
    resta = operador01 + operador02
    mult = operador01 * operador02
    div = operador01/operador02
except:
    print("no se puede colocar operador con valor = 0")

try:    
    print(f"Suma: {suma} \nresta: {resta}\nmultiplicacion: {mult}\ndivision: {div}")
except:
    print("no se pueden mostrar los resultados")