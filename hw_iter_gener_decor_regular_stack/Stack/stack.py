class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

    def push(self, element):
        self.stack.append(element)

    def pop(self, element):
        pop = self.stack.pop(element)
        return pop

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)