import random

class Stack:
    def __init__(self):
        self.items = list()

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

def a(i):
    j = 9
    print(i,j)
def b(k):
    a(1)
    print(k)
def main():
    print("start")
    b(3)

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self, data):
#         if not self.head:
#             self.head = Node(data)
#             return
#         current = self.head
#         while current.next: # if next node exist
#             current = current.next
#         current.next = Node(data)
#     def search(self, target):
#         current = self.head
#         while current.next:
#             if current.data == target:
#                 return True
#             else:
#                 current = current.next
#         return False
#     def remove(self, target):
#         if self.head.data == target:
#             self.head = self.head.next
#         current = self.head
#         previous = None
#         while current:
#             if current.data == target:
#                 previous.next = current.next
#                 break
#             else:
#                 previous = current
#                 current = current.next
#     def __str__(self):
#         node = self.head
#         while node is not None:
#             print(node.data)
#             node = node.next
#         return "end"

from collections import deque

d = deque()
d.append(7)
d.append(-11)
d.append(8)

def check_bracket(expr: str) -> bool:
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        if char not in table:
            print(char)
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            print(char)
            return False
        else:
            print(char)
            pass
    return len(stack) == 0

#queue
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

        # self.front = None
        # self.rear = None
        # self._size = 0

    def enqueue(self, data):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

        # self._size = self._size + 1
        # node = Node(data)
        # if self.rear is None:
        #     self.front = node
        #     self.rear = node
        # else:
        #     self.rear.next = node
        #     self.rear = node

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Empty Queue")
        return self.s1.pop()

        # if self.front is None:
        #     raise IndexError("dequeue from empty queue")
        # self._size = self._size - 1
        # temp = self.front
        # self.front = self.front.next
        # if self.front is None:
        #     self.rear = None
        # return temp.data

    def size(self) -> int:
        return self._size



if __name__ == '__main__':
    {
    # l.append(7)
    # l.append(-11)
    # l.append(8)
    #
    # print(l.__str__())
    # for data in d:
    #     print(data)

    # print(l.search(-11))

    # l = LinkedList()
    # i = 0
    # while i < 20:
    #     n = random.randint(1,28)
    #     l.append(n)
    #     print(n, end=" ")
    #     i = i + 1
    #     print(l)
    #

    # l = LinkedList()
    # l.append(7)
    # l.append(-11)
    # l.append(9)
    #
    # l.remove(-11)
    #
    # print(l)
    }
    # expression = input("Input expression : ")
    # print(check_bracket(expression))

    q = Queue()
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    # print(q.size())
    print(q.dequeue())
    # print(q.size())
    for _ in range(3):
        print(q.dequeue())
