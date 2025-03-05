"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # its just like creating a clone of those nodes 
        # add it like an overhead where 7--> 7 ---> 13 ---> 13 ---> 11 etc 
        # after that i now link that random to it 
        curr = head 
        while curr:
            temp = curr.next 
            new_node = Node(curr.val) 
            curr.next = new_node 
            new_node.next = temp 
            curr = temp 

        # random part 
        curr = head 
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next 
        
        # detach what i added 
        dummy = Node(0)
        curr = head
        new_curr = dummy
        while curr:
            new_curr.next = curr.next 
            new_curr = new_curr.next 
            curr.next = curr.next.next
            curr = curr.next 
        return dummy.next