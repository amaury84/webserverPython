from machine import Pin
import utime 

ledVerde = Pin(2, Pin.OUT)
ledAmarillo = Pin(15, Pin.OUT)
ledRojo = Pin(16, Pin.OUT)
while True:
    ledVerde.on()
    ledAmarillo.off()
    ledRojo.off()
    utime.sleep(5)
    ledVerde.off()
    ledAmarillo.on()
    ledRojo.off()
    utime.sleep(3)
    ledVerde.off()
    ledAmarillo.off()
    ledRojo.on()
    utime.sleep(5)
    ledVerde.off()
    ledAmarillo.on()
    ledRojo.on()
    utime.sleep(2)
    