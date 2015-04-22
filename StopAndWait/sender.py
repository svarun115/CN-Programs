import socket
import os
import signal

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((socket.gethostname(), 20000))
server_sock.listen(1)

'''def handler(signo):
   server_sock.close()
   exit()

signal.signal(signal.SIGINT, handler)'''

#N = int(input("Set Window Size")
N = 5

Sb = 0
Sm = N-1
timer = 0
client, client_add = server_sock.accept()
print("Successful Connection")
while(True):
   timer += 1
   decoded = client.recv(1024).decode('utf8')
   print("Received Request:",int(decoded))
   Rn = int(decoded)
   if(timer < 5):
      timer = 0
      if(Rn > Sb):
         Sm += (Rn - Sb)
         Sb = Rn
         client.send(str(Rn).encode('utf8'))
         print("Sent Sequence No:", Sb)
      if(Sb > 25):
         break
   else:
      timer = 0
      client.send(str(Rn).encode('utf8'))
server_sock.close()
