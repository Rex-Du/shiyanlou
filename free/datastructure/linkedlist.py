class Node:
    """
    链表的节点
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    # def __str__(self):
    #     r =
    def is_empty(self):
        return self.head is None

    def get_len(self):
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next:
            current = current.next
            count += 1
        return count

    def insert(self, index, node):
        if index < 0 or index > self.get_len():
            raise IndexError('index超出范围')
        current = self.head
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            while current.next:
                index -= 1
                if index == 0:
                    node.next = current.next
                    current.next = node
                    break
                current = current.next

    def remove(self, index):
        """
        从任意位置删除一个元素
        :param index:
        :return:
        """
        if index < 0 or index > self.get_len() or self.is_empty():
            raise IndexError('index超出范围')
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                index -= 1
                if index == 0:
                    current.next = current.next.next
                    break
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end='')
            current = current.next
            if current:
                print('-->', end='')
        print('')

    def initlist(self, lst):
        """
        将列表转成链表
        :param lst:
        :return:
        """
        for i in lst:
            node = Node(i)
            self.append(node)


if __name__ == '__main__':
    l = range(10)
    ll = LinkedList()
    ll.initlist(l)
    ll.print_list()
    ll.insert(2, Node(8))
    ll.print_list()
    ll.remove(3)
    ll.print_list()
