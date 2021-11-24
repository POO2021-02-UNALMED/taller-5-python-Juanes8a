from gestion.zoologico import Zoologico


class Zona:
    zoo=[]
    animales=[]
    def __init__(self, nombre,zoo):
        self._nombre=nombre
        Zona.zoo.append(zoo)


    @classmethod        
    def getAnimales(cls):
        return Zona.animales   
    def cantidaAnimales(cls):
        return len(Zona.animales)

    def agregarAnimales(a):
        Zona.animales.append(a)

    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return Zona.zoo[0]            