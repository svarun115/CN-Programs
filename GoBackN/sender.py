import socket
import os
import signal

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((socket.gethostname(), 60001))
server_sock.listen(1)

'''def handler(signo):
   server_sock.close()
   exit()

signal.signal(signal.SIGINT, handler)'''

#N = int(input("Set Window Size")
N = 5

Sb = 0
Sm = N-1

client, client_add = server_sock.accept()
while(True):
   print("Successful COnnection")
   decoded = client.recv(1024).decode('utf8')
   print(decoded)
   Rn = int(decoded)
   if(Rn > Sb):
      Sm += (Rn - Sb)
      Sb = Rn
      client.send(str(Rn).encode('utf8'))
   if(Sb > 25):
      break
server_sock.close()
