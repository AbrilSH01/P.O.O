from tkinter import *

ventana=Tk()
ventana.title("BIENVENIDO")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="#c96363")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="SALDO", bg="#c96363")
lb1.place(x=280, y=40)

lb2=Label(seccion1,text="Su salto actual es: ", bg="#c96363")
lb2.place(x=240, y=150)

boton=Button(seccion1,text="Regresar",fg="black",bg="white")
boton.place(x=265,y=250)
ventana.mainloop()