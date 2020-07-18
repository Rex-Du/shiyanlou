"""
tcp-client:
"""
# author: rexdu
# create: 2020/7/17 18:14
from socket import socket, AF_INET, SOCK_STREAM

# 定义客户端套接字
tcp_client_sock = socket(AF_INET, SOCK_STREAM)
# 向服务器发送连接请求，IP 地址为服务器的 IP 地址
# 注意 connect 方法的参数为元组
tcp_client_sock.connect(('localhost', 1234))

# 连接成功后，进入发送/接收数据循环
while True:
    data = input('输入内容：')
    if not data:
        break
    # 发送二进制数据
    tcp_client_sock.send(data.encode())
    # 接收二进制数据
    data = tcp_client_sock.recv(1024)
    if not data:
        break
    print(data.decode())
# 关闭客户端套接字
tcp_client_sock.shutdown(2)
tcp_client_sock.close()
