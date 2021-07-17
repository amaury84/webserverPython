import machine
import time
pin4 = machine.Pin(2, machine.Pin.OUT)
pin4.value(1)
while True:
    pin4.on()
    time.sleep(0.5)
    pin4.off()
    time.sleep(0.5)
    
