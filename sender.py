import packet
import socket

def send():
   Sb = 0
   Sm = N-1
   while(True):
      p = receive();
      if(p.Rn > Sb):
         Sm = Sm + (Rn - Sb)
         Sb = Rn
      if(
