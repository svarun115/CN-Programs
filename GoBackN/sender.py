import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((socket.gethostname(), 65535))
server_sock.listen(1)

#N = int(input("Set Window Size")
N = 5

Sb = 0
Sm = N-1
while(True):
   client, client_add = server_sock.accept()
   #print("Successful COnnection")
   decoded = (server_sock.recv(1024).decode())
   print(decoded)
   Rn = int(decoded)
   if(Rn > Sb):
      Sm += (Rn - Sb)
      Sb = Rn
   
