from machine import Pin, TouchPad
import utime

def main():
    entradaT = TouchPad(Pin(4))
    entradaT.config(600)
    """
    while True:
    datos = entradaT.read()
    print(datos)
    utime.sleep(0.5)
    with open("logs.txt","a") as file:
        file.write(str(datos)+"\n")
    """
    with open("logs.txt","a") as file:
        print(file.read())
        
if __name__=="__main__":
    main()