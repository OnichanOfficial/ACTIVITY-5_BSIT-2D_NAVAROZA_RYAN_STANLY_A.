# circular_array_queue.py
class CircularArrayQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue full CircularArrayQueue")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue empty CircularArrayQueue")
        val = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return val

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue empty: cannot peek_front")
        return self.data[self.front]

    def __str__(self):
        arr = []
        for i in range(self.size):
            idx = (self.front + i) % len(self.data)
            arr.append(self.data[idx])
        return str(arr)
