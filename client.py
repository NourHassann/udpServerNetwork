import socket


socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
number=0

while True:
    number+=1
    number = str(number)
    socket.sendto(number.encode('utf-8'),("192.168.1.6",2023))
    data=socket.recvfrom(1024)[0].decode('utf-8')
    print(data)
    number =int(number)
 

socket.close()