from machine import Pin
import dht 
import network
import utime
import urequests

led = Pin(2, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("esp32", "prueba_esp32") # Connect to an AP

while not wifi.isconnected():
    print(".",end="")
    utime.sleep(1)
        
print(wifi.ifconfig())

while True:
    utime.sleep(2)
    print("ingresa el dato a enviar")
    dato = input()
    url=""
    url += dato
    r = urequests.get(url)
    print(r.json())
                
if __name__=="__main__":
    main()


