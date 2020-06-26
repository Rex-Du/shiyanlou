"""
author: rexdu
create: 2020/6/26 12:53
"""
import abc


# class Question:
#     def __init__(self, admin=False):
#         self._admin = admin
#
#     def show(self):
#         if self._admin:
#             return "显示问题内容和编辑按钮"
#         return "显示问题内容"


class ABCShow(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass


class UserShow(ABCShow):
    def show(self):
        return "显示问题内容"


class AdminShow(ABCShow):
    def show(self):
        return "显示问题内容和编辑按钮"


class Question:
    def __init__(self, show):
        self._show = show

    def show(self):
        return self._show.show()


if __name__ == '__main__':
    # q1 = Question()
    # print(q1.show())
    # print('===============')
    # q2 = Question(True)
    # print(q2.show())
    user_show = UserShow()
    question_1 = Question(user_show)

    admin_show = AdminShow()
    question_2 = Question(admin_show)
    print(question_1.show())
    print('======================')
    print(question_2.show())
