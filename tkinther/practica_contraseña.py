from tkinter import *
from verificacion import*
import tkinther as tk
from tkinter import tkk
from tkinter import messagebox

#Datos de la ventana
ventana=Tk()
ventana.title("GENERADOR DE CONTRASEÑAS")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="#C093D9")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="CONTRASEÑAS", bg="#C093D9")
lb1.place(x=250, y=40)

lon=Label(seccion1,text="Ingrese la longitud: ", bg="#C093D9")
lon.place(x=110, y=110)
car=Label(seccion1,text="¿Desea incluir caracteres?: ", bg="#C093D9")
car.place(x=100, y=180)

lg=Entry(seccion1)
lg.place(x=280, y=110)

cr=Entry(seccion1)
cr.place(x=280,y=180)

validacion=generador(lg,cr,caracteres,longitud)
boton=Button(seccion1,text="Entrar",fg="black",bg="white",command= validacion.generador)
boton.place(x=265,y=250)




ventana.mainloop()