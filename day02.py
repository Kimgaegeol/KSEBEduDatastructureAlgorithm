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

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next: # if next node exist
            current = current.next
        current.next = Node(data)

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "end"

from collections import deque

d = deque()
d.append(7)
d.append(-11)
d.append(8)

if __name__ == '__main__':
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)
    #
    # print(l.__str__())
    # for data in d:
    #     print(data)

    print(l.search(-11))