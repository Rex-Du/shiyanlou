"""
author: rexdu
create: 2020/6/27 10:47
"""
import abc


class VmReceiver:
    def start(self):
        print("Virtual machine start")

    def stop(self):
        print("Virtual machine stop")


class Command:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass


class StartVmCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.start()


class StopVmCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.stop()


class ClientInvoker:
    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    vmreceiver = VmReceiver()
    start_command = StartVmCommand(vmreceiver)
    stop_command = StopVmCommand(vmreceiver)
    client_invoker = ClientInvoker(start_command)
    client_invoker.do()

    print('============================')
    client_invoker.command = stop_command
    client_invoker.do()
