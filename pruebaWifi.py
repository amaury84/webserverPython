import network
import utime
import urequests
from machine import Pin

def main():
    entrada = Pin(4, Pin.IN, Pin.PULL_UP)
    ledInterno = Pin(2,Pin.OUT)
    ledInterno.off()
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    redes = wifi.scan()
    for i in redes:
        print(i[0].decode(),i[2],i[3])
        
    wifi.connect("esp32", "prueba_esp32") # Connect to an AP

    while not wifi.isconnected():
        print(".",end="")
        utime.sleep(1)
        
    print(wifi.ifconfig())
    contador = 0
    while True:
            utime.sleep(1)
            datos = entrada.value()
            print(datos)
            if datos== 0:
                contador +=1        
                ledInterno.value(contador%2)
                r = urequests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
                print(r.json()["url"])
                
if __name__=="__main__":
    main()

        