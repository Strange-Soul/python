# Network Programming
#https://www.py4e.com/lessons/network

from socket import *
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
import socket
T_PORT=60
TCP_IP='127.000.000.011'
BUF_SIZE=30
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((TCP_IP,T_PORT))
soc.listen(1)
con,addr=soc.accept()
print("Connection Address is :",addr)
while True:
    data=con.recv(BUF_SIZE)
    if not data:
     break
    print("Recived data",data)
con.send(data)

