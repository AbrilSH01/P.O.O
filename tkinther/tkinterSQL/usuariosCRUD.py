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
    #Para borrar el usuario anterior al buscar otro
    textBus.delete(1.0,tk.END)
    if(rsUsu):
        for usu in rsUsu:
         cadena=str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])
         #Para insertar la variable en una nueva linea de texto
         textBus.insert(tk.END,cadena+'\n')
    else: 
        messagebox.showerror("Error","El nombre no existe en la base de datos")

#Funcion que usa mi objeto entre los 2 archivos 
def consultarUsuario():
    cnUsu=controlador.consultarUsuarios()
    #Borrar el contenido anterior
    tabla.delete(*tabla.get_children())
    
    for usu in cnUsu:
       # Crear una tupla con los valores del usuario
        fila = (usu[0], usu[1], usu[2], usu[3])

        # Insertar la fila en la tabla
        tabla.insert("", tk.END, values=fila)
       

#Función que usa mi objeto entre los dos archivos para actualizar
def ejecutarEliminar():
    controlador.eliminarUsuario(varID1.get())

def actualizarUsuario():
    controlador.actualizarUsuario(varID.get(),nombre.get(),correo.get(),contraseña.get())
    


#Inicio de ventana
ventana=Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("600x300")

panel=ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)
pestaña4=ttk.Frame(panel)
pestaña5=ttk.Frame(panel)

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
entryCon=Entry(pestaña1,textvariable=varCon,show='*').pack()

btnGuardar=Button(pestaña1,text="Guardar usuario",command=ejecutaInsert).pack()

#Pestaña 2: Buscar usuarios

titulo2=Label(pestaña2,text="Buscar usuario",fg="green",font=("Modern",18)).pack()

varBus=tk.StringVar()
lblid=Label(pestaña2,text="Identificador de Usuario: ").pack()
txtid=Entry(pestaña2,textvariable=varBus).pack()
btnBusqueda=Button(pestaña2,text="Buscar",command=ejecutarSelectU).pack()

subBus=Label(pestaña2,text="Registrado: ",fg="blue",font=("Modern",15)).pack()
textBus=tk.Text(pestaña2,height=5,width=52)
textBus.pack()


#Pestaña 3: Consultar usuarios
titulo3=Label(pestaña3,text="Consultar usuarios",fg="Red",font=("Modern",18)).pack()
btnConsultar=Button(pestaña3,text="Consultar",command=consultarUsuario).pack()
subCon=Label(pestaña3,text="Usuarios: ",fg="white",font=("Modern",12)).pack()

#Creacion de la tabla
tabla=ttk.Treeview(pestaña3,columns=("id","nombre","correo","contraseña"))
tabla.heading("id",text="ID")
tabla.heading("nombre",text="Nombre")
tabla.heading("correo",text="Correo")
tabla.heading("contraseña",text="Contraseña")
tabla.pack()

#Pestaña 4: Actualización de usuarios
titulo4=Label(pestaña4,text="Actualizar usuarios",fg="Purple",font=("Modern",18)).pack()
subAct=Label(pestaña4,text="Ingrese los datos del usuario actualizar").pack()

varID=tk.StringVar()
lbID=Label(pestaña4,text="ID: ").pack()
txtid=Entry(pestaña4,textvariable=varID).pack()

nombre= tk.StringVar()
lbnombre=Label(pestaña4,text="Nombre: ").pack()
entrynombre=Entry(pestaña4,textvariable=nombre).pack()

correo= tk.StringVar()
lbcorreo=Label(pestaña4,text="Correo: ").pack()
entrycorreo=Entry(pestaña4,textvariable=correo).pack()

contraseña= tk.StringVar()
lbcontraseña=Label(pestaña4,text="Contraseña: ").pack()
entrycontraseña=Entry(pestaña4,textvariable=contraseña).pack()

btnAct=Button(pestaña4,text="Actualizar",command=actualizarUsuario).pack()


#Pestaña 5: Eliminacion de usuarios
titulo4=Label(pestaña5,text="Eliminar usuarios",fg="orange",font=("Modern",18)).pack()
subEli=Label(pestaña5,text="Ingrese el ID del usuario a eliminar").pack()
varID1=tk.StringVar()
txtid=Entry(pestaña5,textvariable=varID).pack()
btnEliminar=Button(pestaña5,text="Eliminar",command=ejecutarEliminar).pack()




panel.add(pestaña1,text="Agregar usuarios")
panel.add(pestaña2,text="Buscar usuario")
panel.add(pestaña3,text="Consultar usuarios")
panel.add(pestaña4,text="Actualizar usuarios")
panel.add(pestaña5,text="Eliminar usuarios")
ventana.mainloop()