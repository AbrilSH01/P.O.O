from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBDEX:
    
    def __init__(self):
        pass
    
    def conexionBDEX(self):
        try:
            conexion=sqlite3.connect("/Users/AbrilHdez/Documents/GitHub/P.O.O/tkinther/tkinterSQL/FPOO/BDExportaciones.db")
            print ("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def guardaTransporte(self,transporte,aduana):
        #Llamar al método conexión
        conx=self.conexionBDEX()
        
        #Validar vacios
        if(transporte=="" or aduana==""):
            messagebox.showwarning("¡Advertencia!","Formulario incompleto")
            conx.close()
        else:
            #Realizar insert BD
            cursor=conx.cursor()
            datos=(transporte,aduana)
            sqlInsert="insert into TBPedimentos (Transporte,Aduana) values (?,?)"
            
            cursor.execute(sqlInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Éxito","Información guardada")
            
    
    def eliminarDatos(self,id):
        conx2=self.conexionBDEX()
        
        try:
            confirmacion=messagebox.askyesno("Confirmacion", "¿Estás seguro de que quieres eliminar los datos de la BD?")
            if confirmacion ==True:
                cursor2 = conx2.cursor()
                cursor2.execute("DELETE FROM TBPedimentos WHERE id = ?", (id,))
                conx2.commit()
                messagebox.showinfo("Información", "Los datos se eliminaron correctamente")
                conx2.close()
            else:
                messagebox.showinfo("Aviso", "Los datos no se han eliminado")
        except sqlite3.OperationalError:
                print("Error de eliminacion.")  
                
    
    
    def consultarDatos(self,aduana):
        conx3=self.conexionBDEX()
        if(aduana== ""):
            messagebox.showwarning("Cuidado","Escribe un nombre")
            conx3.close()
        else:
            try:
                cursor3=conx3.cursor()
                sqlSelect="select * from tbRegistrados where Aduana= "+aduana
                cursor3.execute(sqlSelect)
                CDatos=cursor3.fetchall()
                conx3.close()
                return CDatos
            except sqlite3.OperationalError:
                print("Error de consulta")