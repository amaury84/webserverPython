import _thread
import time
from machine import Pin

led = Pin(2, Pin.OUT)
tiempo=0.5
def ActivarLed():
  while True:
    led.on()
    time.sleep(tiempo)
    led.off()
    time.sleep(tiempo)
 
_thread.start_new_thread(ActivarLed, ())

def mensajes():
    while True:
        print("Hola Mundo!!!")
        time.sleep(2)

_thread.start_new_thread(mensajes, ())

def mensajesNuevos():
    while True:
        print("Tienes un Nuevo Mensaje")
        time.sleep(4)

_thread.start_new_thread(mensajesNuevos, ())