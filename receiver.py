import packet
import socket



def request(Rn):




def receive(p):
   Rn = 0
   while(True):
      if(p.Rn == Rn):
         accept(p)
         Rn += 1
         request(Rn)
      else:
         #drop packet
         request(Rn)

conn, addr =  socket.accept()

if name=="__init__":
