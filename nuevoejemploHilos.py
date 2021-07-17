import _thread
import time
from machine import Pin


def ActivarLed(pin,t):
    led = Pin(pin, Pin.OUT)
    tiempo=t
    while True:
        led.on()
        time.sleep(tiempo)
        led.off()
        time.sleep(tiempo)
 
_thread.start_new_thread(ActivarLed, (2,1))
_thread.start_new_thread(ActivarLed, (4,0.5))
_thread.start_new_thread(ActivarLed, (15,2))