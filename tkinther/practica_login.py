from tkinter import *

correo="121037785@upq.edu.mx"
password="password1234"

#1. Funcion para el mensaje de advertencia

def validacion():
    if correo == email.get() and password == contraseña.get():
        messagebox.showinfo("Bienvenido cardenal!")
    else:
        messagebox.showinfo("Error, los datos son incorrectos!")
        
