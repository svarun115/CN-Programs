import socket
import os
import signal
import random

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((socket.gethostname(), 6008))
server_sock.listen(1)

N = 5

Sb = 0
Sm = N-1

client, client_add = server_sock.accept()
print("Successful Connection")
count = 1
while(True):
   decoded = client.recv(1024).decode('utf8')
   print("Received Request:",int(decoded))
   Rn = int(decoded)
   if(Rn > Sb):
      Sm += (Rn - Sb)
      Sb = Rn
   if(count%5!=0):
      client.send(str(Rn).encode('utf8'))
   else:
      client.send(str(random.randint(1,25)).encode('utf8'))
      print("Sent Sequence No:", Sb)
   if(Sb > 25):
      break
   count +=1
server_sock.close()
