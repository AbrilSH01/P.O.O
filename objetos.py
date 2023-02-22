from Personaje import *
print("SOLICITUD DATOS HEROE")
especieH=input("Escribe la especie de heroe: ")
nombreH=input("Ingrese el nombre del heroe: ")
alturaH=float(input("Ingrese la altura del heroe: "))
recargaH=int(input("Escribe las balas de heroe: "))
print("\n")
print("SOLICITUD DATOS VILLANO")
especieV=input("Escribe la especie de villano: ")
nombreV=input("Escribe la especie de villano: ")
alturaV=float(input("Ingrese la altura del villano: "))
recargaV=int(input("Ingrese las balas del villano: "))


#1.Crear los objetos
heroe=Personaje(especieH,nombreH,alturaH)
villano=Personaje(especieV,nombreV,alturaV)

#2.Usamos los atributos de heroe y villano
print("\n")
print("DATOS HEROE")
print("El personaje se llama: "+heroe.nombre)
print("El personaje pertenece a la especie: "+heroe.especie)
print("El personaje mide: "+str(heroe.altura))
heroe.correr(True)
heroe.lanzar_granadas()
heroe.recargar_arma(recargaH)
print("\n")
print("DATOS VILLANO")
print("El personaje se llama: "+villano.nombre)
print("El personaje pertenece a la especie: "+villano.especie)
print("El personaje mide: "+str(villano.altura))
villano.correr(True)
villano.lanzar_granadas()
villano.recargar_arma(recargaV)




