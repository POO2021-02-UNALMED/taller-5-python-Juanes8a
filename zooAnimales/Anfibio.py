from animal import Animal
class Anfibio(Animal):
    ranas=0
    salamandras=0
    listado=[]
    
    def __init__(self, nombre, edad, habitat, genero,colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Animal._totalAnimales+=1
        Anfibio.listado.append(self)

    def movimiento(self):
        return "saltar"

    def getColorPiel(self):
        return self._colorPiel   
    def isVenenoso(self):
        return self._venenoso
    @classmethod        
    def getAnfibios(cls):
        return Anfibio.listado

    def crearRana(self,nombre,edad,genero):
        Anfibio.ranas+=1
        return Anfibio(nombre,edad,genero,habitat="selva",colorPiel="rojo",venenoso=True)
    def crearSalamandra(self,nombre,edad,genero):
        Anfibio.salamandras+=1
        return Anfibio(nombre,edad,genero,habitat="selva",colorPiel="negro",venenoso=False)  
