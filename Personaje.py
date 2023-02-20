class Personaje:
    #Atributos
    especie="Humano"
    nombre="MasterChief"
    altura=2.70
    
    #Métodos
    def correr(self,status):
        if(status):
            print("El personaje "+ self.nombre + "está corriendo.")
        else:
            print("El personaje "+self.nombre+ "se detuvo.")
            
    def lanzar_granadas(self):
        print("El personaje "+ self.nombre + "lanzó la granada.")
        
    def recargar_arma(self,municiones):
        cargardor=10
        cargador=cargador+municiones
        print("El arma recargada tiene "+cargador+ "balas.")