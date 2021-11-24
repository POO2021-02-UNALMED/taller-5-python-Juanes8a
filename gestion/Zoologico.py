from zooAnimales.Animal import Animal
from gestion.Zona import Zona

class Zoologico:
    zonas=[]

    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion

    def cantidadTotalAnimales(self):
        total=0
        for i in Zoologico.zonas:
            total+=len(Zona.getAnimales())
        return total
    def agregarZonas(self,z):
        Zoologico.zonas.append(z)

    @classmethod        
    def getZonas(cls):
        return Zoologico.zonas          

    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion