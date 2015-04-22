import socket
import signal
import os

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((socket.gethostname(), 6008))
Rn = 1
print("Requested:", Rn)
client_sock.send(str(Rn).encode())

while(True):
   Sn = int(client_sock.recv(1024).decode('utf8'))
   print("Decoded", Sn)
   if(Sn == Rn):
      print("Accepted Packet No:", Sn)      
      Rn += 1
      print("Requested:", Rn)
      client_sock.send(str(Rn).encode('utf8'))
   else:
      print("Dropped Packet", Sn)
      print("Requested:", Rn)
      client_sock.send(str(Rn).encode())
   if(Sn == 25):
      break
client_sock.close()
