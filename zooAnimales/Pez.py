from animal import Animal
class Pez(Animal):
    salmones=0
    bacalaos=0
    listado=[]

    def __init__(self, nombre, edad, habitat, genero,colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Animal._totalAnimales+=1
        Pez.listado.append(self)



    def movimiento(self):
        return "nadar"
    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    @classmethod        
    def getPeces(cls):
        return Pez.listado  



    def crearHalcon(self,nombre,edad,genero):
        Pez.salmones+=1
        return Pez(nombre,edad,genero,habitat="oceano",colorEscamas="rojo",cantidadAletas=6)
    def crearAguilas(self,nombre,edad,genero):
        Pez.bacalaos+=1
        return Pez(nombre,edad,genero,habitat="oceano",colorEscamas="gris",cantidadAletas=6)          