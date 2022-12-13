class LinkedList():
    def __init__(self):
        self.key = None
        self.value = None
        self.pre = None
        self.next = None
        self.ref = 0

class BufferPool:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = LinkedList()
        self.tail = LinkedList()
        self.head.next = self.tail
        self.tail.pre = self.head

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add_node(self, node):
        node.pre = self.head
        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node

    def move_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        tail = self.tail.pre
        self.remove_node(tail)
        return tail

    def get(self, key):
        if key in self.cache:
            self.move_head(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_head(self.cache[key])
        else:
            node = LinkedList()
            node.key = key
            node.value = value
            self.add_node(node)
            self.cache[key] = node
            self.size += 1
            if self.capacity < self.size:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1

if __name__ == '__main__':
    bp = BufferPool(3)
    bp.put("k1", "v1")
    bp.put("k2", "v2")
    bp.put("k3", "v3")
    bp.put("k4", "v4")
    print(bp.get("k4"))
    print(bp.get("k3"))
    print(bp.get("k2"))
    print(bp.get("k1"))
