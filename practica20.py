"""
* Desarrolla una funcion que tomando el diccionario de notas que devuelve la funcion 
creada en la practica 19, genere un PDF con las calificaciones finales del alumnado.
* El pdf debe constar de 3 columnas
    * La primera columna aparecera el numero de lista del alumno o alumna
    * La segunda columna contendra el nombre y apellido
    * la tercera coulmna contendra la nota final
"""

from practica19 import calcular_notas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#Recive la notas de la practica 19
def imprime_notas (notas):
    w,h = A4

    #Crear pdf
    pdf = canvas.Canvas("nota_final.pdf",pagesize=A4)
    
    #3 cabezaras, primero nombre, 
    linea = h - 50
    pdf.setFontSize(16)
    pdf.drawString(50,linea, "N°")
    pdf.drawString(100,linea,"Apellidos y nombre")
    pdf.drawString(400, linea, "Nota final")
    
    i = 1 #Numero del alumno para incrementarlo
    pdf.setFontSize(14)
    
    #bucle para ir tomando todas las claves de notas
    for alumno in notas: #Es el numero de iteraciones basados en el diccionario que se crea
        linea = linea - 20
        pdf.drawString(50,linea, str(i)) # Se coloca el numero del incremento por cada iteracion
        pdf.drawString(100,linea,alumno) # se escribe en cada itercion el nombre del alumno extraido del diccionario notas
        pdf.drawString(400,linea,str(notas[alumno])) #Extraemos el valor del diccionario de la nota final dependiendo del valor del alumno(nombre)
        i = i + 1 #incrementar
    pdf.save() #Salvar archivo
    
notas = calcular_notas("calificaciones.xlsx")
imprime_notas(notas)