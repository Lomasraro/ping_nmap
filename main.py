import platform
import subprocess
import socket

"""Función similar a NMAP"""

fichero = open('direcciones.txt')
ips = fichero.readline().split()
for ip in ips:
    print("Dirección IP escaneada: " + ip)
    for port in range(20, 200):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     result = s.connect_ex((ip, port))
     if result == 0:
        print(port)
        print("Puerto abierto")
     else:
        print(port)
        print("Puerto no abierto")
     s.close()

""""Ping a las IP encontradas"""
"""
def myping(host):
    parametrer = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', parametrer, '4', host]
    response = subprocess.call(command)

    if response == 0:
        print("Host "+host+" encontrado")
    else:
        print("host "+host+" no encontrado")

fichero = open('direcciones.txt')
ips = fichero.readline().split()
for ip in ips:
    print("Hacemos ping a la IP "+ ip)
    myping(ip)
"""