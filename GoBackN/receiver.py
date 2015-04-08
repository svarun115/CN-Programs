import socket
import signal
import os

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((socket.gethostname(), 60001))

'''def handler(signo):
   server_sock.close()
   exit()
signal.signal(signal.SIGINT, handler)'''
Rn = 1
#First Request
client_sock.send(str(Rn).encode())

while(True):

   Sn = int(client_sock.recv(1024).decode('utf8'))
   print("Decoded", Sn)
   if(Sn == Rn):
      print("Accepted Packet No:", Sn)
      Rn += 1
      client_sock.send(str(Rn).encode('utf8'))
   else:
      #drop packet
      client_sock.send(str(Rn).encode())
   if(Sn == 25):
      break
client_sock.close()
