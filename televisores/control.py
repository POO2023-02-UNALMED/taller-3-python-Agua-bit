

class Control:
    

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv = tv

    def turnOn(self, estado: bool):
        self.tv._estado = True

    def turnOff(self, estado: bool):
        self.tv._estado = False

    def canalUp(self):
        self.tv.canalUp(self)

    def canalDown(self):
        self.tv.canalDown(self)

    def volumenUp(self):
        self.tv.volumenUp(self)

    def volumenDown(self):
        self.tv.volumenDown(self)

    def setCanal(self, canal: int):
        self.tv.setCanal(canal)

    def setVolumen(self, volumen: int):
        self.tv.setVolumen(volumen)