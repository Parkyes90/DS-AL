from queue import Queue


class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        print("Deque is Empty")


if __name__ == "__main__":
    deque = Deque()
    print(f"is Deque Empty? : {deque.is_empty()}")
    print("add number 0 ~ 9 to Deque")
    for i in range(10):
        deque.enqueue(i)
    print(f"Deque size {deque.size()}")
    print(f"Deque pop {deque.dequeue()}")
    print(f"Deque peek {deque.peek()}")
    print(f"is Deque Empty? : {deque.is_empty()}")
    print(deque)
    print(deque.dequeue_front())
    deque.enqueue_back(50)
    print(deque.peek())
    print(deque)
