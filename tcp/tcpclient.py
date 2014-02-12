import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.connect(server_address)

try:
    message = "coin_acceptor.insert_coin"
    sock.sendall(message)
finally:
    sock.close()
