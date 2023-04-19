from tkinter import*
from tkinter import ttk
import tkinter as tk
from controladorBDEX import*

controlador=controladorBDEX()

def EjecutarInserts():
    controlador.guardaTransporte(varTra.get(),varAdu.get())

def ejecutarEliminar():
    controlador.eliminarDatos(varEli.get())
    
def consultarDatos():
    cnUsu=controlador.consultarDatos(varCon.get())
    #Borrar el contenido anterior
    tabla.delete(*tabla.get_children())
    
    for usu in cnUsu:
       # Crear una tupla con los valores del usuario
        fila = (usu[0], usu[1], usu[2], usu[3])

        # Insertar la fila en la tabla
        tabla.insert("", tk.END, values=fila)
    
    
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

btnGuardar=Button(pestaña1,text="Guardar informacion",command=EjecutarInserts).pack()


#2. Eliminación 
titulo2=Label(pestaña2,text="ELIMINACIÓN",fg="orange",font=("Modern",18)).pack()
varEli=tk.StringVar()
lblEli=Label(pestaña2,text="Ingrese el ID de los datos a eliminar: ").pack()
txtEli=Entry(pestaña2,textvariable=varEli).pack()
btnEliminar=Button(pestaña2,text="Eliminar",command=ejecutarEliminar).pack()


#3. Consultar por aduana
titulo3=Label(pestaña3,text="CONSULTAR",fg="Red",font=("Modern",18)).pack()
varCon=tk.StringVar()
subCon=Label(pestaña3,text="Inserte el nombre de la aduana: ").pack()
txtCon=Entry(pestaña3,textvariable=varCon).pack()
btnConsultar=Button(pestaña3,text="Consultar",command=consultarDatos).pack()
subCon=Label(pestaña3,text="Datos: ",fg="white",font=("Modern",12)).pack()

#Creacion de la tabla
tabla=ttk.Treeview(pestaña3,columns=("id","Transporte","Aduana"))
tabla.heading("id",text="ID")
tabla.heading("Transporte",text="Transporte")
tabla.heading("Aduana",text="Aduana")
tabla.pack()


panel.add(pestaña1,text="Insertar datos")
panel.add(pestaña2,text="Eliminar")
panel.add(pestaña3,text="Consultar por Aduana")

ventana.mainloop()