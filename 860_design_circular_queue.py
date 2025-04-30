class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev 
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = Node()
        self.tail = Node()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        my_node = Node(value)
        if self.isEmpty():
            self.head.next = my_node
            my_node.prev = self.head
            my_node.next = self.tail
            self.tail.prev = my_node
        else:
            tmp = self.tail.prev
            self.tail.prev = my_node
            tmp.next = my_node
            my_node.prev = tmp
            my_node.next = self.tail
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            # FIFO which means remove at head
            tmp = self.head.next
            frr = tmp.next
            self.head.next = frr
            frr.prev = self.head
            self.size -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()