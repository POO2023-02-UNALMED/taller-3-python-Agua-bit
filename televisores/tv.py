from televisores.control import Control
from televisores.marca import Marca


class TV:

    
    numTV = 0

    def __init__(self, marca: Marca, estado: bool):
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.control : Control 
        self.marca = marca
        self.estado = estado
        self.numTV += 1

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

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    @classmethod
    def setNumTV(cls):
        cls.numTV += 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado == True:
            if 1 <= self.canal and self.canal <= 120:
                self.canal += 1

    def canalDown(self):
        if self.estado == True:
            if 1 <= self.canal and self.canal <= 120:
                self.canal -= 1

    def volumenUp(self):
        if self.estado == True:
            if 0 <= self.volumen and self.volumen <= 7:
                self.volumen += 1

    def volumenDown(self):
        if self.estado == True:
            if 0 <= self.volumen and self.volumen <= 7:
                self.volumen -= 1