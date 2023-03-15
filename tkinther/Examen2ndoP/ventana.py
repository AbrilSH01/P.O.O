from tkinter import*
from tkinter import messagebox

#Creacion de la ventana


ventana=Tk()
ventana.title("BIENVENIDO")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="#c96363")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="INGRESA TUS DATOS", bg="#c96363")
lb1.place(x=280, y=40)

nombre=Button(seccion1,text="Nombre: ",fg="black",bg="white")
nombre.place(x=250,y=100)

app=Button(seccion1,text="Apellido Paterno",fg="black",bg="white")
app.place(x=250,y=170)

apm=Button(seccion1,text="Apellido Materno",fg="black",bg="white")
apm.place(x=250,y=240)

año=Button(seccion1,text="Año de nacimiento",fg="black",bg="white")
año.place(x=250,y=310)

carrera=Button(seccion1,text="Carrera",fg="black",bg="white")
carrera.place(x=250,y=310)

ventana.mainloop()
