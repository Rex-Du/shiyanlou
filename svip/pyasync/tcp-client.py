"""
tcp-client:
"""
# author: rexdu
# create: 2020/7/17 18:14

from socket import socket, SOCK_STREAM, AF_INET

tcp_client_sock = socket(AF_INET, SOCK_STREAM)

tcp_client_sock.connect(('localhost', 1234))

while True:
    data = input("input data to send:")
    if not data:
        break
    tcp_client_sock.send(data.encode())

    data = tcp_client_sock.recv(1024)
    if not data:
        break
    print(data.decode())

tcp_client_sock.close()


