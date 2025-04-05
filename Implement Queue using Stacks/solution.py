class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current:
            s = str(current.item) + ' ' + s
            current = current.next
        return 'bottom -> ' + s + '<- top'


class MyQueue:
    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def push(self, x):
        self.left.push(x)

    def pop(self):
        if self.empty():
            raise ValueError('Queue is empty')

        if self.right.is_empty():
            while not self.left.is_empty():
                self.right.push(self.left.pop())

        return self.right.pop()

    def peek(self):
        if self.empty():
            raise ValueError('Queue is empty')

        if self.right.is_empty():
            while not self.left.is_empty():
                self.right.push(self.left.pop())

        return self.right.peek

    def empty(self):
        return self.left.is_empty() and self.right.is_empty()
