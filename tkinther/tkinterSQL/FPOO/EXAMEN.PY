from tkinter import*
from tkinter import ttk
import tkinter as tk
from controladorBDEX import*

controlador=controladorBDEX

def EjecutarInserts():
    controlador.guardaTransporte(varTra.get(),varAdu.get())
    
ventana=Tk()
ventana.title("EXPORTACIONES")
ventana.geometry("600x300")

panel=ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)


#1 Registro de trasnporte y aduana
titulo=Label(pestaña1,text="REGISTRO",fg="blue",font=("Modern",18)).pack()
varTra= tk.StringVar()
lblTra=Label(pestaña1,text="Inserte el tipo de transporte: ").pack()
entryTra=Entry(pestaña1,textvariable=varTra).pack()

varAdu=tk.StringVar()
lblAdu=Label(pestaña1,text="Inserte el nombre de la aduana: ").pack()
entryAdu=Entry(pestaña1,textvariable=varAdu).pack()

btnGuardar=Button(pestaña1,text="Guardar transporte",command=EjecutarInserts).pack()


panel.add(pestaña1,text="Insertar datos")
panel.add(pestaña2,text="Eliminar")
panel.add(pestaña3,text="Consultar por Aduana")

ventana.mainloop()