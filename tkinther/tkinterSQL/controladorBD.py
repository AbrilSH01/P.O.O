from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("/Users/AbrilHdez/Documents/GitHub/P.O.O/tkinther/tkinterSQL/registro_usuarios")
            print("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def guardarUsuario(self,nom,cor,con):
        #Llamar al método conexión
        conx=self.conexionBD()
        
        #Validar vacios
        if(nom=="" or cor=="" or con==""):
            messagebox.showwarning("Aguas!!","Formulario incompleto")
            conx.close()
        else:
            #Realizar insert BD
            #Preparamos las variables necesarias
            cursor=conx.cursor()
            conH=self.encriptarContra(con)
            datos=(nom,cor,conH)
            sqlInsert="insert into tbRegistrados(nombre,correo,contra) values(?,?,?)"
            
            #Ejecutamos el insert y cerramos la conexion
            cursor.execute(sqlInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Éxito","Usuario guardado")
            
    #Convertir la contraseña a bytes
    def encriptarContra(self,con):
        
        #Preparar la contraseña y la sal para Hash
        conPlana=con
        conPlana=conPlana.encode()
        sal=bcrypt.gensalt()
        
        #Encriptar
        conHa=bcrypt.hashpw(conPlana,sal)
        print(conHa)
        
        #Regresar la contraseña encriptada
        return conHa