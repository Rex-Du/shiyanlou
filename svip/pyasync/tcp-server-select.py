"""
tcp-server-select:
"""
# author: rexdu
# create: 2020/7/17 20:58
import time
import select
from socket import socket, AF_INET, SOCK_STREAM

tcp_server_sock = socket(AF_INET, SOCK_STREAM)
tcp_server_sock.setblocking(False)
tcp_server_sock.bind(('', 1234))
tcp_server_sock.listen()

rlist = [tcp_server_sock]
wlist = []
xlist = []

print('waiting for connection...')

while True:
    print('----------------------------')
    print('rlist:', [f'sock fd: {s.fileno()}' for s in rlist])
    print('wlist:', [f'sock fd: {s.fileno()}' for s in wlist])

    try:
        readable, writable, exceptional = select.select(rlist, wlist, xlist)
    except KeyboardInterrupt:
        break

    print('readable:', ['套接字FD {}'.format(s.fileno()) for s in readable])
    print('writable:', ['套接字FD {}'.format(s.fileno()) for s in writable])

    for sock in readable:
        # TCP 服务端的套接字有两种，一种是等待客户端连接的主套接字
        # 另一种是负责处理连接后的一系列事务的临时套接字
        # 如果是主套接字有情况，甭问，肯定是有客户端连接请求，它就是干这个的
        # 这种情况，主套接字的 accept 方法会返回一个新建临时套接字
        if sock is tcp_server_sock:
            tcp_extension_sock, addr = sock.accept()
            print(f'connected: {addr}')
            rlist.append(tcp_extension_sock)
        # 如果有情况的不是主套接字，那就是临时套接字了
        # 肯定是客户端发来消息了，接收消息
        # 接收完毕，该套接字自动可写就绪，也就是要把它放到 wlist 列表里
        # 下一个 while 循环就处理这个可写套接字
        else:
            data = sock.recv(1024)
            if data:
                print(f'recv: {data.decode()}')
                if sock not in wlist:
                    wlist.append(sock)
            else:
                rlist.remove(sock)
                sock.close()

    for sock in writable:
        print('server send ...')
        sock.send(f'{time.ctime()}'.encode())
        wlist.remove(sock)

    for sock in exceptional:
        print('exceptional sock', sock)
        rlist.remove(sock)
        if sock in wlist:
            wlist.remove(sock)
        sock.close()

tcp_server_sock.close()
