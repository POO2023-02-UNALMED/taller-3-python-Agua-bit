

class Control:
    
    def enlazar(self, tv: tv):
        self.tv = tv
        self.tv.setControl(self)

    def getTv(self):
        return self.tv
    
    def setTv(self, tv: tv):
        self.tv = tv

    def turnOn(self, estado: bool):
        self.tv.estado = True

    def turnOff(self, estado: bool):
        self.tv.estado = False

    def canalUp(self):
        if self.tv.estado == True:
            if 1 <= self.tv.canal and self.tv.canal <= 120:
                self.tv.canal += 1

    def canalDown(self):
        if self.tv.estado == True:
            if 1 <= self.tv.canal and self.tv.canal <= 120:
                self.tv.canal -= 1

    def volumenUp(self):
        if self.tv.estado == True:
            if 0 <= self.tv.volumen and self.tv.volumen <= 7:
                self.tv.volumen += 1

    def volumenDown(self):
        if self.tv.estado == True:
            if 0 <= self.tv.volumen and self.tv.volumen <= 7:
                self.tv.volumen -= 1

    def setCanal(self, canal: int):
        if self.tv.estado == True:
            if 1 <= canal and canal <= 120:
                if 1 <= self.tv.canal and self.tv.canal <= 120:
                    self.tv.canal = canal

    def setVolumen(self, volumen: int):
        if self.tv.estado == True:
            if 0 <= volumen and volumen <= 7:
                if 0 <= self.tv.volumen and self.tv.volumen <= 7:
                    self.tv.volumen = volumen