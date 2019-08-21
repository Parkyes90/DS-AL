from node import Node


class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

    def _add_first(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    def _delete_first(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결 리스트가 비었습니다.")

    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node

        self.tail = node

    def add_node(self, value):
        if not self.head:
            self._add_first(value)
        else:
            self._add(value)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def delete_node(self, index):
        if not self.head or not self.head.pointer:
            self._delete_first()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print(f"인덱스 {index}에 해당하는 노드가 없습니다.")

    def delete_node_by_value(self, value):
        if not self.head or not self.head.pointer:
            self._delete_first()
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print(f"값 {value}에 해당하는 노드가 없습니다.")


if __name__ == "__main__":
    ll = LinkedListFIFO()
    for i in range(1, 5):
        ll.add_node(i)
    ll.print()
    ll.delete_node(2)
    ll.print()
    ll.add_node(15)
    ll.print()
    for i in range(ll.length - 1, -1, -1):
        ll.delete_node(i)
    print("삭제")
    ll.print()
