class DLL:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash_map = {}
        self.head = DLL(-1, -1)
        self.tail = DLL(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_head(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = temp
        temp.prev = node


    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.delete_node(node)
        self.insert_at_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self.delete_node(node)
            self.insert_at_head(node)
        else:
            node = DLL(key, value)
            if len(self.hash_map) == self.capacity:
                del self.hash_map[self.tail.prev.key]
                self.delete_node(self.tail.prev)
                self.insert_at_head(node)
            else:
                self.insert_at_head(node)
            self.hash_map[key] = node



        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)