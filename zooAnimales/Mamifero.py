from Animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    listado=[]

    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje=pelaje
        self._patas=patas
        Animal._totalAnimales+=1
        Mamifero.listado.append(self)



    def isPelaje(self):
        return self._pelaje==True  
    def getPatas(self):
        return self._patas
    @classmethod        
    def getMamiferos(cls):
        return Mamifero.listado


    def crearCaballo(self,nombre,edad,genero):
        Mamifero.caballos+=1
        return Mamifero(nombre,edad,genero,habitat="praderas",pelaje=True,patas=4)
    def crearLeones(self,nombre,edad,genero):
        Mamifero.leones+=1
        return Mamifero(nombre,edad,genero,habitat="selva",pelaje=True,patas=4)          