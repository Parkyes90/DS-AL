from linked_list_fifo import LinkedListFIFO


class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._create_hash_table()

    def _create_hash_table(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item % self.size

    def _add(self, item):
        index = self._find(item)
        self.slots[index].add_node(item)

    def _delete(self, item):
        index = self._find(item)
        self.slots[index].delete_node_by_value(item)

    def print(self):
        for i in range(self.size):
            print(f"슬롯(slot){i}: ")
            self.slots[i].print()


def test_hash_tables():
    h1 = HashTableLL(3)
    for i in range(0, 20):
        h1._add(i)
    h1.print()
    h1._delete(0)
    h1._delete(1)
    h1._delete(2)
    h1.print()


if __name__ == "__main__":
    test_hash_tables()
