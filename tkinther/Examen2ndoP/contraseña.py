from tkinter import*
from tkinter import messagebox
from random import choice
digitos="1234567890"
año_act="2023"
longitud=3
p=""
class Contraseña:
    def __init__(self,nombre,app,apm,año,carrera,digitos,año_act):
        self.nombre=nombre
        self.app=app
        self.apm=apm
        self.año=año
        self.carrera=carrera
        self.digitos=digitos
        self.año_act=año_act
        self.longitud=longitud
        
    def generador(self):
        
        #Digitos del año actual
        año_actual=str(año_act)[-2:]
    
         #Digitos de fecha de nacimiento
        fecha_nacimiento=str(self.año)[-2:]
    
        #Letras del nombre
        letra_nombre=str(self.nombre)[0]
    
        #Letras del apellido P
        letra_apellidoP=str(self.app)[0]
    
        #Letras del apellido M
        letra_apellidoM=str(self.apm)[0]
    
        #Digitos aleatorios
        digitos_aleatorios=p.join([choice(self.digitos) for i in range (longitud)])
    
        #Letras de carrera
        letra_carrera=str(self.carrera)[:3]
    
        matricula=año_actual+fecha_nacimiento+letra_nombre+letra_apellidoP+letra_apellidoM+digitos_aleatorios+letra_carrera
    
        messagebox.showinfo("Contraseña","Su contraseña es: "+matricula)