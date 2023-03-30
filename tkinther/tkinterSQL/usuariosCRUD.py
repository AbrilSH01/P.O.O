from tkinter import*
from tkinter import ttk
import tkinter as tk
from controladorBD import*

#Instancia:puente entre los dos archivos
controlador=controladorBD()

#Metodo que usa mi obj entre los 2 archivos
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())
    
    
 #Funcion que usa mi objeto entre los 2 archivos  
def ejecutarSelectU():
    controlador.consultarUsuario(varBus.get())
    rsUsu=controlador.consultarUsuario(varBus.get())
    for usu in rsUsu:
     cadena=str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])
     resultado=cadena.get()
    if(rsUsu):
        print(cadena)
    
    else: 
        messagebox.showerror("Error","El nombre no existe en la base de datos")
    
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
lblCor=Label(pestaña1,text="Correo: ").pack()
entryCor=Entry(pestaña1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon=Label(pestaña1,text="Contraseña: ").pack()
entryCon=Entry(pestaña1,textvariable=varCon).pack()

btnGuardar=Button(pestaña1,text="Guardar usuario",command=ejecutaInsert).pack()

#Pestaña 2: Buscar usuarios

titulo2=Label(pestaña2,text="Buscar usuario",fg="green",font=("Modern",18)).pack()

varBus=tk.StringVar()
lblid=Label(pestaña2,text="Identificador de Usuario: ").pack()
txtid=Entry(pestaña2,textvariable=varBus).pack()
btnBusqueda=Button(pestaña2,text="Buscar",command=ejecutarSelectU).pack()

subBus=Label(pestaña2,text="Registrado: ",fg="blue",font=("Modern",15)).pack()
textBus=tk.Text(pestaña2,height=5,width=52).pack()







panel.add(pestaña1,text="Agregar usuarios")
panel.add(pestaña2,text="Buscar usuario")
panel.add(pestaña3,text="Consultar usuarios")
panel.add(pestaña4,text="Actualizar usuario")

ventana.mainloop()