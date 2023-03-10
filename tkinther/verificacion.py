from tkinter import *
from tkinter import messagebox
from random import choice
caracteres="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
caractEsp="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&¡+*"
longitud=8
p=""
class generador:
    
    def __init__(self,lg,cr,caracteres,caractEsp,longitud,p):
        self.lg=lg
        self.cr=cr
        self.caracteres=caracteres
        self.caractEsp=caractEsp
        self.longitud=longitud
        self.p=p
        
    def generador(self):
        lg=int(self.lg.get())
        cr=self.cr.get()
        if cr=="si" and lg=="":
            p = ""
            p=p.join([choice(self.caractEsp) for i in range (int(self.longitud))])
            print (p)
            messagebox.showinfo("Contraseña","Su contraseña es: "+p)
        elif cr=="no" and lg=="":
            p = ""
            p=p.join([choice(self.caracteres) for i in range (int(self.longitud))])
            print (p)
            messagebox.showinfo("Contraseña","Su contraseña es: "+p)
        elif cr=="si" and lg==lg:
            p = ""
            p=p.join([choice(self.caractEsp) for i in range (lg)])
            print (p)
            messagebox.showinfo("Contraseña","Su contraseña es: "+p)            
        elif cr=="no" and lg==lg:
            p = ""
            p=p.join([choice(self.caracteres) for i in range (lg)])
            print (p)
            messagebox.showinfo("Contraseña","Su contraseña es: "+p)

        