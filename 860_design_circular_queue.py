class Node:
    def __init__(self,val,prev=None,next=None):
        self.val = val 
        self.prev = prev
        self.next = next 

class MyCircularQueue:

    def __init__(self, k: int):
        # im thinking of using a double linked list 
        # i now get the head and the tail 
        # i have a count pos to keep track of k anytime i add a node 
        self.k = k 
        self.size = 0 
        self.head = None 
        self.tail = None 

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.head.prev = self.tail 
            self.head.next = self.tail 
            self.tail.prev = self.head 
            self.tail.next = self.head 
        else:
            self.tail.next = newNode
            newNode.prev = self.tail 
            newNode.next = self.head # this is because it is circular so it goes back to head 
            self.head.prev = newNode
            self.tail = newNode
        self.size += 1 
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
            self.head.prev = self.tail 
            self.tail.next = self.head # this is because it is circular 
        self.size -= 1 
        return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1 
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1 
        return self.tail.val  

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True 
        return False

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