from machine import Pin
from time import sleep
import dht 
 
sensor = dht.DHT11(Pin(4))
led = Pin(2, Pin.OUT)
while True:
  try:
    sleep(2)
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    string = "Temperature: " +str(t)+","+"Humidity: "+str(h)+"\n"
    with open("datos.txt","a") as file:
        file.write(string)
    print('Temperature: %3.1f C' %t)
    print('Humidity: %3.1f %%' %h)
    if t > 19:
        led.on()
    else:
        led.off()
  except OSError as e:
    print('Sensor Reading Failed')