from tkinter import *
from tkinter import messagebox

correo="121037785@upq.edu.mx"
password="password1234"

#1. Funcion para el mensaje de advertencia

def validacion():
    if correo == email.get() and password == contraseña.get():
        messagebox.showinfo("Bienvenido cardenal!")
    else:
        messagebox.showinfo("Error, los datos son incorrectos!")
        
#Datos de la ventana
ventana=Tk()
ventana.title("INICIO DE SESION")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="#2596be")
seccion1.pack(expand=True,fill='both')

lb1=Label(seccion1,text="INICIO DE SESIÓN")
lb1.pack()

correo=Label(seccion1,text="Correo electrónico: ")
correo.place(x=205, y=60)
password=Label(seccion1,text="Contraseña: ")
password.place(x=180, y=90)

email=Entry(seccion1)
email.place(x=250, y=80)

contraseña=Entry(seccion1)
contraseña.config(show="*")
contraseña.place(x=260,y=95)


