from televisores.marca import Marca
from televisores.control import Control

class Tv():

    canal = 1
    volumen = 1
    precio = 500
    control : Control 
    numTV = 0

    def __init__(self, marca: Marca, estado: bool):
        self.marca = marca
        self.estado = estado

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getCanal(self):
        return self.canal
    
    def setCanal(self, canal):
        self.canal = canal
    
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio = precio 

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        self.volumen = volumen

    def getControl(self):
        return self.control
    
    def setControl(self, control):
        self.control = control

    def getNumTV(self):
        return self.numTV
    
    def setNumTV(self):
        self.numTV += 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        self.canal += 1

    def canalDown(self):
        self.canal -= 1

    def volumenUp(self):
        self.volumen += 1

    def volumenDown(self):
        self.volumen -= 1