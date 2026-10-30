# array_stack.py
class ArrayStack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1  

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push to full ArrayStack")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop empty ArrayStack")
        val = self.data[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack empty: cannot peek")
        return self.data[self.top]

    def __str__(self):
        return str(self.data[:self.top + 1])
