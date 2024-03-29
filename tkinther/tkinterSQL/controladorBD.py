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
            conx.close()
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
    
    def consultarUsuario(self,id):
        #1. Realizar la conexión BD
        conx2=self.conexionBD()
        
        #2. Verificar que el id esté vacío
        if(id== ""):
            messagebox.showwarning("Cuidado","Escribe un identificador")
            conx2.close()
        else:
            #3. Proceder a la cosulta
            try:
                #4. Preparamos lo necesario
                cursor2=conx2.cursor()
                sqlSelect="select * from tbRegistrados where id= "+id
                
                #5. Ejecutamos y cerramos conexion
                cursor2.execute(sqlSelect)
                RSusuario=cursor2.fetchall()
                conx2.close()
                return RSusuario
            except sqlite3.OperationalError:
                print("Error de consulta")
                
    def consultarUsuarios(self):
        conx3=self.conexionBD()
        try:
            cursor3=conx3.cursor()
            sqlSelect="select * from tbRegistrados"
        
            cursor3.execute(sqlSelect)
            CUsuario=cursor3.fetchall()
            conx3.close()
            return CUsuario
        except sqlite3.OperationalError:
                print("Error de consulta todos.")
                
    def actualizarUsuario(self,id,nom,cor,con):
        conx4=self.conexionBD()
        try:
            cursor4=conx4.cursor()
            cursor4.execute("UPDATE tbRegistrados SET nombre =?,correo=?,contra=? WHERE id=?",(nom,cor,con,id))
            conx4.commit()
            AUsuario=cursor4.fetchall()
            conx4.close()
            messagebox.showinfo("Exito","El usuario ha sido actualizado")
            return AUsuario
        except sqlite3.OperationalError:
                print("Error de actualizacion.")   

    def eliminarUsuario(self, id):
        conx5 = self.conexionBD()
        try:
            #Se le pregunta al usuario si quiere seguir con la eliminacion
            respuesta=messagebox.askyesno("Confirmacion", "¿Estás seguro de que quieres eliminar el usuario de la BD?")
            if respuesta ==True:
                cursor5 = conx5.cursor()
                cursor5.execute("DELETE FROM tbRegistrados WHERE id = ?", (id,))
                conx5.commit()
                messagebox.showinfo("Información", "El usuario se eliminó correctamente")
                conx5.close()   
            else:
                messagebox.showinfo("Aviso", "El usuario no se eliminó, vuelva a intentarlo después") 
        except sqlite3.OperationalError:
                print("Error de eliminacion.")         
               
            
    
            