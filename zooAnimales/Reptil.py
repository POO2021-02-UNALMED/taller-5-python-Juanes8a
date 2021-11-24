from animal import Animal
class Reptil(Animal):
    iguanas=0
    serpientes=0
    listado=[]

    def __init__(self, nombre, edad, habitat, genero,colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Animal._totalAnimales+=1
        Reptil.listado.append(self)

    def movimiento(self):
        return "reptar"
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola
    @classmethod        
    def getReptiles(cls):
        return Reptil.listado      

    def crearIguana(self,nombre,edad,genero):
        Reptil.iguanas+=1
        return Reptil(nombre,edad,genero,habitat="humedal",colorEscamas="cafe glorioso",largoCola=3)
    def crearSerpiente(self,nombre,edad,genero):
        Reptil.serpientes+=1
        return Reptil(nombre,edad,genero,habitat="jungla",colorEscamas="blanco y amarillo",largoCola=1)            