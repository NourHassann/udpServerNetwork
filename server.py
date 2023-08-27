import socket as sock


Host = '192,168,1,6'
port = 2023

server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
server.bind(Host, port)
server.listen()
client_socket , address = server.accept()
message = client_socket.recv(1024).decode('utf-8')