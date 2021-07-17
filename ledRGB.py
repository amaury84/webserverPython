from machine import Pin
import utime 

ledRGBRojo = Pin(2, Pin.OUT)
ledRGBVerde = Pin(15, Pin.OUT)
ledRGBAzul = Pin(16, Pin.OUT)

def tiempo(n=1):
    if n <=0:
        n=1
    utime.sleep(n)
    
def rojo():
    ledRGBRojo.on()
    ledRGBAzul.off()
    ledRGBVerde.off()
    print("color rojo activado")

def verde():
    ledRGBRojo.off()
    ledRGBAzul.off()
    ledRGBVerde.on()
    print("color verde activado")
    
def azul():
    ledRGBRojo.off()
    ledRGBAzul.on()
    ledRGBVerde.off()
    print("color azul activado")

def violeta():
    ledRGBRojo.on()
    ledRGBAzul.on()
    ledRGBVerde.off()
    print("color violeta activado")
    
def apagado():
    ledRGBRojo.off()
    ledRGBAzul.off()
    ledRGBVerde.off()
    print("RGB Apagado")

for i in range(5):
    apagado(
    tiempo()
    verde()
    tiempo()
    rojo()
    tiempo()
    violeta()
    tiempo()
    azul()
    tiempo()
