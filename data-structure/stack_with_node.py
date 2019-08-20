class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        print("Stack is empty")

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        print("Stack is empty")

    def size(self):
        return self.count

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


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
    stack.print()
