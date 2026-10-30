# linked_queue.py
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        from node import Node
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue empty LinkedQueue")
        val = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue empty: cannot peek_front")
        return self.front.value

    def __str__(self):
        curr = self.front
        arr = []
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return str(arr)
