# Network Programming
#https://www.py4e.com/lessons/network
import socket
host='data.pr4e.org'
port=80
address=(host,port)
my_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_sock.connect(address)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

while True:
    data=my_sock.recv(1024)
    if len(data)<1:
      break
    print(data.decode(data),end="")
my_sock.close()
'''from socket import *
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
'''
