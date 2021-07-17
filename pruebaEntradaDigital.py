from machine import Pin
import utime
entrada = Pin(4, Pin.IN, Pin.PULL_UP)
ledInterno = Pin(2,Pin.OUT)
ledInterno.off()

contador = 0
while True:
    utime.sleep(1)
    datos = entrada.value()
    print(datos)
    if datos== 0:
        contador +=1        
        ledInterno.value(contador%2)