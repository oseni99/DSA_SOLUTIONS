# LRU Cache requires you to keep track of double linked lists so it helps with O(1) insertion & deletion
# create the double linked list class
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        # adding at left removig at right
        prev = self.right.prev
        nxt_node = self.right
        prev.next = node
        node.prev = prev
        node.next = nxt_node
        nxt_node.prev = node

    def remove(self, node):
        # get the previous and next
        prev = node.prev
        nxt_node = node.next
        prev.next = nxt_node
        nxt_node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #  where i check if the cache is more than the limit
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)