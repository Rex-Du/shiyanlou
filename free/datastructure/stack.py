class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self._stack = list()

    def push(self, value):
        if len(self._stack) < self.capacity:
            self._stack.append(value)
        else:
            raise ValueError('ck full')

    def pop(self):
        if self.is_empty():
            raise IndexError('stack empty')
        else:
            return self._stack.pop()

    def is_empty(self):
        return self._stack.__len__() == 0

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]

    def size(self):
        return self._stack.__len__()


def balanced_parentheses(parentheses):
    """
    判断括号是否成对
    :param parentheses:
    :return:
    """
    stack = Stack(len(parentheses))
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            stack.pop()
    return stack.is_empty()


if __name__ == '__main__':
    print(balanced_parentheses('((((((((())))'))
