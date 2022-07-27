from cProfile import label
from sre_parse import State
from tabnanny import verbose
from tkinter import *
from tkinter.ttk import *
from turtle import circle
from controlador import *
from tkinter.messagebox import *

def añadir():
    cantidad = int(sbNumbero.get())
    if twProductos.focus() == "":
        showerror("Error","Selecciona algun producto")
    elif cantidad == 0:
        showerror("Error", "La cantidad seleccionada no puede ser 0")
    else:
        index = int(twProductos.focus().split("I")[1],16) - 1 # devuelve lo siguiente Fila - I001, I00A devuelve la fila en hexadecimal
        producto = productos[index]
        importe = round(cantidad * producto[2],2)
        añadir_linea(twCarrito,txtTotal,producto,cantidad,importe)
        sbNumbero.delete(0,"end")
        sbNumbero.insert(0,0)
        carrito.append([producto[0],producto[1],producto[2],cantidad])

def finalizar():
    cliente = cmbCliente.get()
    if cliente == "":
        showerror("Error","Seleccionar un cliente")
    elif len(carrito) == 0:
        showerror("Error", "Seleecionar cantidad de articulos")
    else:        
        try:
            dniClient = cliente.split("-")[0]
            nombreCliente = cliente.split("-")[1]
            finalizar_pedido(carrito, dniClient,nombreCliente)
            twCarrito.delete(*twCarrito.get_children()) #Borra toda las lineas de twCarrito
            carrito.clear()
            showinfo("","El pedido a sido realizado")
        except:
            showerror("Error","error al realizar el pedido")
            
clientes = []
productos = []
carrito = []

ventana = Tk(className="Proyecto")
ventana.title("Proyecto Final")
ventana.geometry("800x500")
ventana.resizable(False,False)

lblCliente = Label(ventana, text="Cliente")
lblCliente.place(x=100,y=20, in_=ventana)

cmbCliente = Combobox(ventana, width=80, state="readonly")
cmbCliente.place(x=160, y=20, in_=ventana)
clientes = cargar_clientes(cmbCliente)

lblProdcuto = Label(ventana, text="Productos")
lblProdcuto.place(x=140, y=90, in_=ventana)

twProductos = Treeview(ventana, height=15)
twProductos["columns"] = ("#1")
twProductos.column("#0",width=180)
twProductos.column("#1",width=60)
twProductos.heading("#0",text="Nombre")
twProductos.heading("#1",text="Precio")
twProductos.place(x=60, y=120, in_=ventana)
productos = cargar_productos(twProductos)

sbNumbero = Spinbox(ventana,from_=0, to=10 , width=5)
sbNumbero.place(x=330,y=200,in_=ventana)
sbNumbero.insert(0,0)

btnComprar = Button(ventana, text=">>", width=5, command=añadir)
btnComprar.place(x=330,y=250, in_=ventana)

lblCarrito = Label(ventana, text="Carrito de la compra")
lblCarrito.place(x=520,y=90, in_=ventana)

twCarrito = Treeview(ventana, height=15)
twCarrito["columns"] = ("#1","#2") # "#0" esta por default
twCarrito.column("#0",width=200)
twCarrito.column("#1",width=60)
twCarrito.column("#2",width=80)
twCarrito.heading("#0",text="Nmbre")
twCarrito.heading("#1",text="cant.")
twCarrito.heading("#2",text="Importe")
twCarrito.place(x=400,y=120,in_=ventana)

btnFinalizar = Button(ventana, text="Finzalizar compra",width=20, command=finalizar)
btnFinalizar.place(x=400,y=450,in_=ventana)

lblTotal = Label(ventana,text="Total")
lblTotal.place(x=600,y=450,in_=ventana)

txtTotal = Entry(ventana,width=10, justify=RIGHT)
txtTotal.place(x=650,y=450,in_=ventana)
txtTotal.insert(END,"0.0 $")
txtTotal.config(state="readonly")

ventana.mainloop()