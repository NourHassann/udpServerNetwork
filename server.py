from pickle import TRUE
import socket as sock


Host = '192.168.1.6'
port = 2023

server = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
server.bind((Host, port))
while TRUE: 
     message , address = server.recvfrom(1024)
     print(message.decode('utf-8'))
     server.sendto(f"packet{message.decode('utf-8')} is received".encode('utf-8'), address)