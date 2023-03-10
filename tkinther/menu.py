from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.title("BIENVENIDO")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="#c96363")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="MENÚ", bg="#c96363")
lb1.place(x=280, y=40)

boton1=Button(seccion1,text="Consultar saldo",fg="black",bg="white")
boton1.place(x=250,y=100)

boton2=Button(seccion1,text="Ingresar efectivo",fg="black",bg="white")
boton2.place(x=250,y=170)

boton3=Button(seccion1,text="Retirar efectivo",fg="black",bg="white")
boton3.place(x=250,y=240)

boton4=Button(seccion1,text="Depositar a otra cuenta",fg="black",bg="white")
boton4.place(x=250,y=310)

ventana.mainloop()