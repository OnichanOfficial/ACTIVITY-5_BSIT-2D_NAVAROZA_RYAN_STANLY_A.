# linked_stack.py
class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        from node import Node
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop empty LinkedStack")
        val = self.top.value
        self.top = self.top.next
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack empty: cannot peek")
        return self.top.value

    def __str__(self):
        curr = self.top
        arr = []
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return str(arr)
