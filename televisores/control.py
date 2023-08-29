import tv

class Control:

    tv = tv
    
    def enlazar(self, tv: tv):
        self.tv = tv
        self.tv.control = Control

    def getTv(self):
        return self.tv
    
    def setTv(self, tv: tv):
        self.tv = tv
    

        
