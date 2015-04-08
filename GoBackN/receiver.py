import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((socket.gethostname(), 65535))

Rn = 0
#First Request
client_sock.send(str(Rn).encode())

while(True):
   Sn = int(client_sock.recv(1024).decode())
   if(Sn == Rn):
      print("Accepted Packet No:", Sn)
      Rn += 1
      client_sock.send(str(Rn).encode())
   else:
      #drop packet
      client_sock.send(str(Rn).encode())

