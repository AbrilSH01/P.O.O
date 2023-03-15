from tkinter import*
from contraseña import*
from tkinter import messagebox

#Creacion de la ventana


ventana=Tk()
ventana.title("BIENVENIDO")
ventana.geometry("600x500")

seccion1=Frame(ventana,bg="#c96363")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="INGRESA TUS DATOS", bg="#c96363")
lb1.place(x=250, y=40)

nombre=Label(seccion1,text="Nombre: ",fg="black",bg="#c96363")
nombre.place(x=110, y=110)
entry1=Entry(seccion1)
entry1.place(x=280, y=110)

app=Label(seccion1,text="Apellido Paterno",fg="black",bg="#c96363")
app.place(x=110, y=180)
entry2=Entry(seccion1)
entry2.place(x=280, y=175)

apm=Label(seccion1,text="Apellido Materno",fg="black",bg="#c96363")
apm.place(x=110, y=260)
entry3=Entry(seccion1)
entry3.place(x=280, y=255)

año=Label(seccion1,text="Año de nacimiento",fg="black",bg="#c96363")
año.place(x=110, y=340)
entry4=Entry(seccion1)
entry4.place(x=280, y=335)

carrera=Label(seccion1,text="Carrera",fg="black",bg="#c96363")
carrera.place(x=110, y=420)
entry5=Entry(seccion1)
entry5.place(x=280, y=420)

validacion=Contraseña(nombre,app,apm,año,carrera,digitos,año_act)
boton=Button(seccion1,text="Ingresar datos",fg="black",bg="white",command=validacion.generador)
boton.place(x=220,y=480)

ventana.mainloop()
