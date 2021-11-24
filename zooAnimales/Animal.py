from Mamifero import Mamifero
from Ave import Ave
from Reptil import Reptil
from Pez import Pez
from Anfibio import Anfibio
class Animal:
    _totalAnimales=0
    zona=[]
    def __init__(self,nombre, edad,habitat, genero) :
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        Animal._totalAnimales+=1

    def movimiento(self):
        return "desplazarse"

    def getNombre(self):
        return self._nombre    
    def getEdad(self):
        return self._edad  
    def getHabitat(self):
        return self._habitat 
    def getGenero(self):
        return self._genero       


    def totalPorTipo(self):
        return 	"Mamiferos: " + str((len(Mamifero.getMamiferos()))) + '\n' +  "Aves: " + str((len(Ave.getAves()))) + '\n' + "Reptiles: " + str(len(Reptil.getReptiles())) + '\n' + "Peces: " + str(len(Pez.getPeces())) + '\n' +"Anfibios: " +  str(len(Anfibio.getAnfibios()))



    #def __str__(self):
    #    if   Animal.zona!=None:
    #         return "Mi nombre es "  + self._nombre +  ", tengo una edad d, " + self._edad + ", habito en " + self._habitat +" y mi genero es " + self._genero + ", la zona en la que me ubico es " + Animal.zona[0].getNombre() + ", en el " + (zona[0].getZoo()).getNombre() 