from tkinter import*
from tkinter import ttk
import tk as tk
import tkinter as tk
from tkinter import messagebox


ventana=Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("600x300")

panel=ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)
pestaña4=ttk.Frame(panel)

#Pestaña 1: Formulario de registro
titulo=Label(pestaña1,text="Registro Usuarios",fg="blue",font=("Modern",18)).pack()
varNom= tk.StringVar()
lblNom=Label(pestaña1,text="Nombre: ").pack()
entryNom=Entry(pestaña1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor=Label(pestaña1,text="Nombre: ").pack()
entryCor=Entry(pestaña1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon=Label(pestaña1,text="Nombre: ").pack()
entryCon=Entry(pestaña1,textvariable=varCon).pack()

btnGuardar=Button(pestaña1,text="Guardar usuario")


panel.add(pestaña1,text="Agregar usuarios")
panel.add(pestaña2,text="Buscar usuario")
panel.add(pestaña3,text="Consultar usuarios")
panel.add(pestaña4,text="Actualizar usuario")

ventana.mainloop()