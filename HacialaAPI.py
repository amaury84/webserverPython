from machine import Pin
import dht 
import network
import utime
import urequests

sensor = dht.DHT11(Pin(4))
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
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    print('tmp:',t)
    print('hum:',h)
    #url=""
    #r = urequests.get()
    #print(r.json()["url"])
                
if __name__=="__main__":
    main()

