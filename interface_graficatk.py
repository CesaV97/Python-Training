#Improtar todo
from argparse import _VersionAction
from cProfile import label
from itertools import tee
from math import comb
from msilib.schema import ListBox
from tkinter import *
from turtle import end_fill, width
from tkinter.ttk import *

def saludar():
    lbl_text.configure(text="Hola boton")
    txt_01.delete(0, END)
    #txt_01.insert(0, "Boton pulsado")
    #txt_01.insert(0, combo.get())
    txt_01.insert(0, listbox.get(ACTIVE))
    
    
#Mostrar ventana
ventana = Tk(className="Interfaze grafica")
ventana.geometry("400x300")

#Etiqueta
lbl_text = Label(ventana, text = "Hola mundo tkinter")
lbl_text.place(x=100, y=0, in_ = ventana)

#Boton
btn_activar = Button(ventana, text="Saludar", command=saludar)
btn_activar.place(x=100, y=50,in_=ventana)

#Caja de texto
txt_01 = Entry(ventana, width=30)
txt_01.place(x=100, y=100, in_=ventana)

#Combobox
combo = Combobox(ventana, width=30)
combo.place(x=100, y=150, in_=ventana)
combo["values"] = (1,2,3,4,5,"Text")
combo.current(1)

#Listbox
listbox = ListBox(ventana, width = 2)
listbox.insert(0,"valor1")
listbox.insert(1,"valor2")
listbox.place(x=100, y=200, in_=ventana)

ventana.mainloop()