from tkinter import *

#1. Generar una ventana
ventana=Tk()
ventana.title("Ejemplo de 3 frames")
ventana.geometry("600x400")

#2. Agregar frames
seccion1=Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="gray")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="purple")
seccion3.pack(expand=True,fill='both')

#3. Agregar botones

botonAzul=Button(seccion1,text="botón azul",fg="blue")
botonAzul.place(x=60,y=60,height=30,width=100)

botonNegro=Button(seccion2,text="botón negro",fg="black")
botonNegro.grid(row=0,column=0)

botonAmarillo=Button(seccion2,text="botón amarillo",fg="yellow")
botonAmarillo.grid(row=1,column=2)

botonVerde=Button(seccion3,text="botón verde",fg="green")
botonVerde.pack()

ventana.mainloop()