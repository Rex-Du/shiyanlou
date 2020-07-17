"""
author: rexdu
create: 2020/6/25 21:13
"""

"""
正常情况下，我们开始一个实验，需要判断一系列前置条件：用户是否已经登录、课程是否满足学习的条件、实验是否满足可以启动等。
如果我们直接将这些对象在客户端 Client 类中使用，无疑增加了客户端类和 User，Course 和 Lab 类的耦合度。
另外如果我们要增加新的前置条件判断时，我们就要修改 Client 类。为了解决这些问题，我们引入了外观模式实现了 FacadeLab 类，在这个类中，
我们通过对外提供接口 FacadeLab.can_be_started 来屏蔽客户端类对子系统的直接访问，使得新的客户端类 NewClient 的代变得简洁。

总地来说外观模式的主要目的在于降低系统的复杂程度，在面向对象软件系统中，类与类之间的关系越多，不能表示系统设计得越好，
反而表示系统中类之间的耦合度太大，这样的系统在维护和修改时都缺乏灵活性，因为一个类的改动会导致多个类发生变化，
而外观模式的引入在很大程度上降低了类与类之间的耦合关系。引入外观模式之后，增加新的子系统或者移除子系统都非常方便，
客户类无须进行修改（或者极少的修改），只需要在外观类中增加或移除对子系统的引用即可。
"""


class Uer:
    def is_login(self):
        return True


class Course:
    def can_be_learned(self):
        return True


class Lab:
    def can_be_started(self):
        return True


class Client:
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def start_lab(self):
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            print('start lab')
        else:
            print('can not start lab')


class FacadeLab:
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def can_be_started(self):
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            return True
        return False


class NewClient:
    def __init__(self, lab):
        self.lab = lab

    def start_lab(self):
        if self.lab.can_be_started():
            print('start lab')
        else:
            print('can not start lab')


if __name__ == '__main__':
    user = Uer()
    course = Course()
    lab = Lab()
    client_1 = Client(user, course, lab)
    client_1.start_lab()
    print('===============================')
    facade_lab = FacadeLab(user, course, lab)
    client_2 = NewClient(facade_lab)
    client_2.start_lab()
