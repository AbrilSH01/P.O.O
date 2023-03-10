from tkinter import *
from tkinter import messagebox
#Datos de la ventana
ventana=Tk()
ventana.title("CAJA POPULAR")
ventana.geometry("600x500")

seccion1=Frame(ventana,bg="#c96363")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="REGISTRATE", bg="#c96363")
lb1.place(x=250, y=40)

n=Label(seccion1,text="Nombre completo: ", bg="#c96363")
n.place(x=110, y=110)
e=Label(seccion1,text="Edad: ", bg="#c96363")
e.place(x=110, y=175)
noc=Label(seccion1,text="No. de cuenta: ", bg="#c96363")
noc.place(x=110, y=240)
s=Label(seccion1,text="Saldo: ", bg="#c96363")
s.place(x=110, y=305)

n=Entry(seccion1)
n.place(x=280, y=110)
e=Entry(seccion1)
e.place(x=280,y=175)
noc=Entry(seccion1)
noc.place(x=280, y=240)
s=Entry(seccion1)
s.place(x=280,y=305)

boton=Button(seccion1,text="Registrar",fg="black",bg="white",)
boton.place(x=265,y=400)


ventana.mainloop()