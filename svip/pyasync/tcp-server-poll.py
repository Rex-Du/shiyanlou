# File Name: server_poll.py

import select
import socket
import time

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setblocking(False)
server_sock.bind(('', 1234))
server_sock.listen()

# 该字典用于存放新建临时分支套接字，key 是文件描述符，value 是套接字
connections = {}

# 创建 poll 对象
poll = select.poll()

# 将主套接字 server_sock 的文件描述符注册到读事件链表里
# 注册套接字描述符之后，poll 会监视套接字的相关活动
# poll.register 方法接收俩参数：套接字的文件描述符、事件位掩码
# 针对套接字的三个事件及其位掩码（正整数）：
# POLLIN 可读 1 ，POLLOUT 可写 4 ，POLLHUP 关闭 16
poll.register(server_sock.fileno(), select.POLLIN)

print('Waiting for connection...')

while True:
    time.sleep(1)
    print('\n========循环开始========')
    try:
        # poll.poll 方法的返回值 events 是列表，列表中保存的是元组
        # 元组内的元素是准备就绪的套接字对应的文件描述符和事件位掩码
        events = poll.poll()
    except KeyboardInterrupt:
        break
    # 获取发生事件的套接字的文件描述符 fd 和事件位掩码 flag
    for fd, flag in events:
        print('--------套接字FD: {} 位掩码: {}'.format(fd, flag))

        # 如果主套接字有事件就绪，一定是可读就绪，它只负责接收客户端连接
        if fd == server_sock.fileno():
            # 接收客户端的连接请求，创建新的临时套接字用来发送和接收数据
            # addr 是元组，元组内是客户端套接字的 IP 地址和端口号
            extension_sock, addr = server_sock.accept()
            print('收到连接，客户端地址:', addr)
            # 将新的临时套接字设置为非阻塞模式
            extension_sock.setblocking(0)
            # 注册新的临时套接字，监视其可读事件
            poll.register(extension_sock.fileno(), select.POLLIN)
            # 把新建临时分支套接字加入到存储连接的字典里
            connections[extension_sock.fileno()] = extension_sock

        # 如果临时套接字可读事件就绪，也就是说客户端发送数据过来
        elif flag & select.POLLIN:
            # 利用文件描述符从存储连接的字典里获取可读事件就绪的临时套接字
            extension_sock= connections[fd]
            # 接收数据这块儿需要注意，如果客户端突然关闭连接
            # 对应的临时套接字会同时可读和关闭就绪，即事件位掩码为 17
            # 此时套接字的 recv 方法在运行时会触发 ConnectionResetError 异常
            # 捕获这个异常，使程序向下执行，顺利关闭套接字
            try:
                data = extension_sock.recv(1024)
            except ConnectionResetError:
                pass
            if data:
                print('套接字 {} 收到数据: {}'.format(fd, data.decode()))
                # 套接字接收数据后，可写事件会立刻就绪
                # poll 转而监视其可写事件，下个 while 循环会处理
                poll.modify(fd, select.POLLOUT)
            else:
                flag = select.POLLHUP

        # 如果套接字可写就绪，也就是套接字收到客户端发来的数据后
        if flag & select.POLLOUT:
            print("套接字 {} 发送数据...".format(fd))
            # 利用文件描述符，从存储连接的字典里获取可读就绪的临时套接字
            extension_sock = connections[fd]
            # 发送数据
            extension_sock.send('收到信息，这是模拟信息'.encode())
            # 套接字向客户端发送消息后，poll 转为监视其可读事件
            poll.modify(fd, select.POLLIN)

        # 如果客户端关闭，临时套接字的关闭事件会就绪
        elif flag & select.POLLHUP:
            print('套接字 {} 关闭'.format(fd))
            # 注销文件描述符对应的套接字，不再监视之
            poll.unregister(fd)
            # 关闭套接字
            connections[fd].close()
            # 将套接字从存储连接的字典里移除
            del connections[fd]

    print('--------connections: {}'.format(list(connections.keys())))
    print('========循环结束========')

# 注销主套接字
poll.unregister(server_sock.fileno())
# 关闭主套接字
server_sock.close()
print('\nEnd')