import network
import utime
ssid="esp32"
passwd="prueba_esp32"
wf = network.WLAN(network.STA_IF) #AP_IF
wf.active(True)
#listaWifi = wf.scan()
#for i in listaWifi:
#    print(i[0].decode())
wf.connect(ssid,passwd)
while not wf.isconnected():
    print(".")
    utime.sleep(1)
print(wf.ifconfig())

import upip
upip.install("paramiko")
import paramiko
# Inicia un cliente SSH
ssh_client = paramiko.SSHClient()
# Establecer política por defecto para localizar la llave del host
localmentessh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Conectarse
ssh_client.connect('192.168.1.100', 22, 'amaury', 'Trigun_28')
# Ejecutar un comando de forma remota capturando entrada, salida y error estándar
entrada, salida, error = ssh_client.exec_command('dir')
# Mostrar la salida estándar en pantalla
print (salida.read())
# Cerrar la conexión
ssh_client.close()