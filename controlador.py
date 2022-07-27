from datetime import datetime
from optparse import Values
from pdb import line_prefix
import re
from sre_parse import State
from accesoBD import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import *
import uuid #trae valores alatoreos

def cargar_clientes(cmbCliente):
    listaclientes = seleccionar_clientes()
    listaClientesFormat = []
    
    for cliente in listaclientes:
        listaClientesFormat.append(str(cliente[0]+"-"+cliente[1]))
        
    cmbCliente["values"]=tuple(listaClientesFormat)  
    return listaclientes

def cargar_productos(twProductos):
    listaProductos = seleccionar_productos()
    
    for producto in listaProductos:
        twProductos.insert("","end",text=producto[1], values=str(producto[2]) + "$")
    return listaProductos

def añadir_linea(twCarrito,txtTotal,producto,cantidad,importe):
    twCarrito.insert("","end",text=producto[1],values=(cantidad,str(importe)))
    total =  round(float(txtTotal.get().split("$")[0])+importe,2)
    txtTotal.config(state="active")
    txtTotal.delete(0,"end")
    txtTotal.insert(0,str(total)+"$")
    txtTotal.config(state="readonly")
    
def finalizar_pedido(carrito, dniClient,nombreCliente):
    idPedido = str(uuid.uuid4())
    insertar_pedido(idPedido,dniClient)
    insertar_lineas_pedido(idPedido,carrito)
    imprimir_ticket(idPedido,carrito,nombreCliente)
    
def imprimir_ticket(idPedido,carrito,nombreCliente):
    w,h = A4 #definir anchura y altura de formato
    pdf = canvas.Canvas(idPedido+".pdf",pagesize=A4)
    linea = h - 100
    pdf.setFontSize(14)
    pdf.drawString(100,linea,"N° Pedido: "+ idPedido)
    linea = linea - 20
    pdf.drawString(100,linea,"Cliente: "+nombreCliente)
    linea = linea -20
    fecha = datetime.now()
    pdf.drawString(100,linea,"Fecha: "+fecha.strftime("%d/%m/%Y %H:%M:%S"))
    
    
    linea = linea - 50 
    
    total = 0
    for elemento in carrito:
        pdf.drawString(140,linea, str(elemento[3])+" x " + elemento[1])
        importe = round(elemento[2]*elemento[3],2)
        pdf.drawString(400,linea,str(importe) + " $")
        linea = linea - 20 
        total = total + importe
        
    pdf.line(100,linea,450,linea)    
    linea = linea - 50
    pdf.setFontSize(22)
    pdf.drawString(150, linea, "Total    " + str(round(total,2)) + " $")
    
    pdf.save()    