class Personaje:
    
    #Agregar constructor al personje
    def __init__(self,esp,nom,alt):
        self.__especie=esp
        self.__nombre=nom
        self.__altura=alt
    
    #Métodos
    def correr(self,status):
        if(status):
            print("El personaje "+ self.__nombre + " está corriendo.")
        else:
            print("El personaje "+self.__nombre+ " e detuvo.")
            
    def lanzar_granadas(self):
        print("El personaje "+ self.__nombre + " lanzó la granada.")
        
    def recargar_arma(self,municiones):
        cargador=10
        cargador=cargador+municiones
        print("El arma recargada tiene "+str(cargador)+ " balas.")

    def __pensar(self):
        print("Estoy pensando..")
    #Gets y sets para un correcto encapsulamiento  
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie=esp
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre=nom
    
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,alt):
        self.__altura=alt
        
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie=esp