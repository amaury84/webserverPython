# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, SoftI2C
import ssd1306, framebuf
import utime

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

columnas = 128
filas = 64
oled = ssd1306.SSD1306_I2C(columnas, filas, i2c)

oled.text('Academia Cisco', 0, 50) #columna , fila
oled.show()

#imagen de 60x31
imagen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x80, 0x00, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x30, 0x00, 0x00, 
0x00, 0x00, 0x80, 0x00, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x30, 0x00, 0x00, 
0x00, 0x60, 0x83, 0x00, 0x18, 0x30, 0x40, 0x00, 0x00, 0x60, 0x83, 0x00, 0x18, 0x30, 0x40, 0x00, 
0x00, 0x60, 0x83, 0x00, 0x18, 0x30, 0x40, 0x00, 0x10, 0x60, 0x83, 0x04, 0x18, 0x30, 0x41, 0x80, 
0x30, 0x60, 0x83, 0x06, 0x18, 0x30, 0x41, 0x80, 0x30, 0x60, 0x83, 0x06, 0x18, 0x30, 0x41, 0x80, 
0x30, 0x60, 0x83, 0x06, 0x18, 0x30, 0x41, 0x80, 0x00, 0x00, 0x80, 0x00, 0x00, 0x30, 0x00, 0x00, 
0x00, 0x00, 0x80, 0x00, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x30, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x3c, 0x00, 0x00, 0x0e, 0x03, 0x00, 0x00, 0x00, 0x7c, 0x30, 0xf8, 0x3e, 0x0f, 0xc0, 0x00, 
0x00, 0xc0, 0x30, 0x80, 0x50, 0x14, 0x60, 0x00, 0x00, 0xc0, 0x30, 0xc0, 0x60, 0x18, 0x30, 0x00, 
0x01, 0x80, 0x30, 0xf0, 0x60, 0x10, 0x30, 0x00, 0x01, 0x80, 0x30, 0x38, 0x60, 0x10, 0x30, 0x00, 
0x00, 0xc0, 0x30, 0x0c, 0x60, 0x18, 0x30, 0x00, 0x00, 0xe4, 0x30, 0x08, 0x70, 0x1c, 0x60, 0x00, 
0x00, 0x7c, 0x30, 0xf8, 0x1e, 0x0f, 0xc0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
buffer = bytearray(imagen)
fb = framebuf.FrameBuffer(buffer,60,31,framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(fb,34,10) #columna, fila
oled.show()               
