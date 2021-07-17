from machine import Pin, PWM
import utime

def main():
    ledVerde = PWM(Pin(15),1000)
    ledVerde.duty(512)
    #ledAzul.on()
    #ledAzul.value(1)
    #ledAzul.value(True)
    for i in range(1023):
        ledVerde.duty(i)
        utime.sleep(0.01)
    for i in range(1023,-1,-1):
        ledVerde.duty(i)
        utime.sleep(0.01)

if __name__ == "__main__":
    main()