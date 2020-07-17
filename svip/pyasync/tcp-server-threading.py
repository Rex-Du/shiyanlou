"""
tcp-server:
"""
# author: rexdu
# create: 2020/7/17 18:08

from socket import socket, AF_INET, SOCK_STREAM
import threading

ip_port = ('', 1234)

# 定义 TCP 服务器套接字
tcp_server_sock = socket(AF_INET, SOCK_STREAM)
"""参数说明：
1、socket_family : 套接字家族

套接字家族	说明
AF_UNIX	基于文件的套接字家族
AF_INET	面向网络的套接字家族
2、socket_type : 套接字传输类型

套接字类型	说明
SOCK_STREAM	创建 TCP 套接字时使用，面向连接，数据流式
SOCK_DGRAM	创建 UDP 套接字时使用，无连接，数据报式
"""
tcp_server_sock.bind(ip_port)
tcp_server_sock.listen()


def handle(sock, addr):
    while True:
        data = sock.recv(1024)
        if not data:
            break
            # data 为二进制对象，将其转换为 UTF-8 格式
        print('收到数据：{}'.format(data.decode()))
        # 临时服务端套接字的 send 方法向客户端发送数据
        # data 为二进制对象，将其转换为 UTF-8 格式，再整体转换为二进制对象
        sock.send('{} {}'.format(
            '[ShiYanLou]', data.decode()).encode())
    sock.close()
    print(f'{addr} closed')


def main():
    while True:
        print("waiting for connection...")
        tcp_extension_sock, addr = tcp_server_sock.accept()

        print(f"connected from: {addr}")
        t = threading.Thread(target=handle, args=(tcp_extension_sock, addr))
        t.start()
    # 主动关闭服务器（正常情况下这步不会发生）
    tcp_server_sock.close()


if __name__ == '__main__':
    main()
