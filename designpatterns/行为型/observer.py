"""
author: rexdu
create: 2020/6/26 16:08
"""
import abc


class Subject:
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Course(Subject):
    def __init__(self):
        super().__init__()
        self._message = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg
        self.notify()


class ObserverBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, subject):
        pass


class UserObserver(ObserverBase):
    def update(self, subject):
        print(f'user observer: {subject.message}')


class OrgObserver(ObserverBase):
    def update(self, subject):
        print(f'organization observer: {subject.message}')


if __name__ == '__main__':
    course = Course()
    user_observer = UserObserver()
    org_observer = OrgObserver()

    course.attach(user_observer)
    course.attach(org_observer)

    course.message = '第一次改变属性'
    course.detach(user_observer)

    print('===============')
    course.message = '第二次改变属性'


