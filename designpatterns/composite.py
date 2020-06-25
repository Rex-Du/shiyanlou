"""
author: rexdu
create: 2020/6/25 10:13
"""
import abc


class Worker(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def work(self):
        pass


class Employee(Worker):
    def work(self):
        print(f'employee {self.name} start to work')


class Leader(Worker):
    def __init__(self, name):
        super().__init__(name)
        self.members = set()

    def add_member(self, employee):
        self.members.add(employee)

    def remove_member(self, employee):
        if employee in self.members:
            self.members.remove(employee)

    def work(self):
        print(f'Leader {self.name} start to work')
        for employee in self.members:
            employee.work()


if __name__ == '__main__':
    employee_1 = Employee('duqing')
    employee_2 = Employee('lifan')
    leader = Leader('guoguo')
    leader.add_member(employee_1)
    leader.add_member(employee_2)
    leader.work()
