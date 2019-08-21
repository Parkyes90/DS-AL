class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        print("Queue is Empty.")

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            # head 주소의 pointer 에 node 가 할당된 후 tail 은 node 로 덮어씀
            self.tail.pointer = node
            self.tail = node

        self.count += 1

    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


if __name__ == "__main__":
    queue = LinkedQueue()
    print(f"is Queue Empty? : {queue.is_empty()}")
    print("add number 0 ~ 9 to Queue")
    for i in range(10):
        queue.enqueue(i)
    print(f"Queue size {queue.size()}")
    for i in range(5):
        print(queue.dequeue())
    print(f"Queue dequeue {queue.dequeue()}")
    print(f"Queue peek {queue.peek()}")
    print(f"is Queue Empty? : {queue.is_empty()}")
    queue.print()
