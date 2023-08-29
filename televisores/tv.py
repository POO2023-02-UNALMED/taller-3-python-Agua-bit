

class TV:

    _numTV = 0

    def __init__(self, marca, estado: bool):
        self._canal = 1
        self._volumen = 1
        self._precio = 500 
        self._marca = marca
        self._estado = estado
        TV._numTV += 1

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):
        if (self._estado == True and 1 <= canal and canal <= 120):
            self._canal = canal
    
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio 

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if (self._estado == True and 0 <= self._volumen and self._volumen <= 7):
            self._volumen = volumen

    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, _numTV):
        cls._numTV = _numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if (self._estado == True and 1 <= self._canal and self._canal < 120):
            self._canal += 1

    def canalDown(self):
        if (self._estado == True and 1 < self._canal and self._canal < 120):
            self._canal -= 1

    def volumenUp(self):
        if (self._estado == True and  0 < self._volumen and self._volumen < 7):
            self._volumen += 1

    def volumenDown(self):
        if (self._estado == True and 0 < self._volumen and self._volumen < 7):
            self._volumen -= 1