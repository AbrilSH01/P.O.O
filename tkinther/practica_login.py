from tkinter import *
from validacion import*
from tkinter import messagebox

correo="121037785@upq.edu.mx"
contraseña="contraseña1234"

#Datos de la ventana
ventana=Tk()
ventana.title("INICIO DE SESION")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="#2596be")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="LOGIN")
lb1.place(x=250, y=40)


c=Label(seccion1,text="Correo electrónico: ")
c.place(x=110, y=110)
p=Label(seccion1,text="Contraseña: ")
p.place(x=150, y=180)

email=Entry(seccion1)
email.place(x=280, y=110)

password=Entry(seccion1)
password.config(show="*")
password.place(x=280,y=180)

#Boton de inicio de sesión
validacion=Login(email,password,correo,contraseña)
boton=Button(seccion1,text="Entrar",fg="black",bg="white",command= validacion.validacion1)
boton.place(x=265,y=250)


print(password)
print(email)
ventana.mainloop()


