class Node:
    def __init__(self, data, nexti=None):
        self.item = data
        self.next = nexti

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.item if self.head else None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item) + ' '
            current = current.next
        return f"start -> {s} <- end"

class MyStack(object):
    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()

    def push(self, x):
        self.queue_1.add(x)

    def pop(self):
        if self.empty():
            raise ValueError("Stack is empty.")
        for _ in range(len(self.queue_1) - 1):
            self.queue_2.add(self.queue_1.pop().item)
        item = self.queue_1.pop().item
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        return item

    def top(self):
        if self.empty():
            raise ValueError("Stack is empty.")
        for _ in range(len(self.queue_1) - 1):
            self.queue_2.add(self.queue_1.pop().item)
        item = self.queue_1.peek
        self.queue_2.add(self.queue_1.pop().item)
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        return item

    def empty(self):
        return len(self.queue_1) == 0
