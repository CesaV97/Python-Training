#Crear un archivo PDF
from reportlab.pdfgen import canvas
#Libreria para agregar tamaño de PDF
from reportlab.lib.pagesizes import A4  
#


w,h = A4 #w = A, h = 4
#Crear archivo pdf
pdf = canvas.Canvas("prueba.pdf",pagesize=A4)

#Escribir una linea en un PDF
pdf.drawString(50,h-50,"Hola Mundo") #Colocar la posicion y la cadena que queremos insertar

#Colcoar en nuestro PDf figuras geometricas
pdf.line(50,500,100,500)
pdf.rect(300,700,50,100)
pdf.circle(100,400,80)

#Como cambiar estilo de la letra, tipo, color, tamaño
pdf.setFillColorRGB(255,0,0)
pdf.setFont("Times-Roman",40) #Fuente, tamaño
pdf.drawString(50, h-75,"!Python¡")

#Guardar archivo PDF
pdf.save()