class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    # 시간 복잡도 O(n)
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        print("Queue is Empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        print("Queue is Empty")

    def __repr__(self):
        return repr(self.items)


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
