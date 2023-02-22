class Personaje:
    
    #Agregar constructor al personje
    def __init__(self,esp,nom,alt):
        self.especie=esp
        self.nombre=nom
        self.altura=alt
    
    #Métodos
    def correr(self,status):
        if(status):
            print("El personaje "+ self.nombre + "está corriendo.")
        else:
            print("El personaje "+self.nombre+ "se detuvo.")
            
    def lanzar_granadas(self):
        print("El personaje "+ self.nombre + "lanzó la granada.")
        
    def recargar_arma(self,municiones):
        cargador=10
        cargador=cargador+municiones
        print("El arma recargada tiene "+str(cargador)+ "balas.")