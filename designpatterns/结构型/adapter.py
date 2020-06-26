"""
如果不用适配器模式，在新式课程类中额外定义一个新的 show 方法不也是一样的吗？其实不然，这个 Adapter 类是独立于任意课程类之外的类，
如果有一天 Page 的接口被修改，接收新式课程类中的三个方法，而且不再接收旧式课程的 show 方法呢？
我们可以直接弃用 Adapter 类，新式类依然不需要任何改动。
"""


class OldCourse:
    def show(self):
        print("show desription")
        print("show teacher of course")
        print("show labs")


class Page:
    def __init__(self, course):
        self.course = course

    def render(self):
        self.course.show()


class NewCourse:
    def show_desc(self):
        print("show description")

    def show_teacher(self):
        print("show teacher of course")

    def show_labs(self):
        print("show labs")


class Adapter:
    def __init__(self, course):
        self.course = course

    def show(self):
        self.course.show_desc()
        self.course.show_teacher()
        self.course.show_labs()


if __name__ == '__main__':
    old_course = OldCourse()
    page = Page(old_course)
    page.render()

    print('=========================')

    new_course = NewCourse()
    page = Page(Adapter(new_course))
    page.render()
