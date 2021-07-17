import utime
from machine import Pin

class LedRGB:
    
    def __init__(self,rojo,azul,verde):
        self.Rojo = Pin(rojo, Pin.OUT)
        self.Azul = Pin(azul, Pin.OUT)
        self.Verde = Pin(verde, Pin.OUT)
    
    def rojo(self):
        #self.Rojo.on()
        print("color rojo activado")

    def azul(self):
        print("color azul activado")

    def verde(self):
        print("color verde activado")
    
    def violeta(self):
        print("color violeta activado")
    
    def apagado(self):
        print("apagado")