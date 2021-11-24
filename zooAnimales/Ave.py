from animal import Animal
class Ave(Animal):
    halcones=0
    aguilas=0
    listado=[]

    def __init__(self, nombre, edad, habitat, genero,colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas=colorPlumas
        Animal._totalAnimales+=1
        Ave.listado.append(self)

    def movimiento(self):
        return "volar"

    def getColorPlumas(self):
        return self._colorPlumas  
    @classmethod        
    def getAves(cls):
        return Ave.listado

    def crearHalcon(self,nombre,edad,genero):
        Ave.halcones+=1
        return Ave(nombre,edad,genero,habitat="montanas",colorPlumas="cafe glorioso")
    def crearAguila(self,nombre,edad,genero):
        Ave.aguilas+=1
        return Ave(nombre,edad,genero,habitat="montanas",colorPlumas="blanco y amarillo")        