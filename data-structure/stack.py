class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        print("Stack is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        print("Stack is empty")

    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(f"is Stack Empty? : {stack.is_empty()}")
    print("add number 0 ~ 9 to stack")
    for i in range(10):
        stack.push(i)
    print(f"stack size {stack.size()}")
    print(f"stack pop {stack.pop()}")
    print(f"stack peek {stack.peek()}")
    print(f"is Stack Empty? : {stack.is_empty()}")
    print(stack)
