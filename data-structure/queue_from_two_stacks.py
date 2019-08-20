class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        print("Queue is empty")

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        print("Queue is empty")

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        print("Queue is empty")

    def is_empty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))


if __name__ == "__main__":
    queue = Queue()
    print(f"is Queue Empty? : {queue.is_empty()}")
    print("add number 0 ~ 9 to Queue")
    for i in range(10):
        queue.enqueue(i)
    print(f"Queue size {queue.size()}")
    print(f"Queue pop {queue.dequeue()}")
    print(f"Queue peek {queue.peek()}")
    print(f"is Queue Empty? : {queue.is_empty()}")
    print(queue)
