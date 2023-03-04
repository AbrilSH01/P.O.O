from tkinter import messagebox

class Login:
    
    def __init__(self,email,password,correo,contraseña):
        
        self.email=email
        self.password=password
        self.correo=correo
        self.contraseña=contraseña
        
    def validacion1(self):
        email=self.email.get()
        password=self.password.get()
        if email==self.correo and password == self.contraseña:
                messagebox.showinfo("¡Bienvenido!", "¡Bienvenido, datos ingresados con éxito!")
                print(email)
                print(password)
        elif email=="" or password=="":
            messagebox.showerror("Error", "Debes de ingresar el correo y contraseña")
            return True
        else:
                messagebox.showerror("Error", "Error,ingresa tus datos nuevamente")
                return False
                

          