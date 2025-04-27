"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # if no node
        if not head:
            return None

        hash_store = {}
        curr = head
        # add the clone to the hash in one pass
        while curr:
            clone = Node(curr.val)
            hash_store[curr] = clone
            curr = curr.next

        # now add the next and randoms
        curr = head
        while curr:
            old = hash_store[curr]
            old.next = hash_store.get(curr.next)
            old.random = hash_store.get(curr.random)
            curr = curr.next

        return hash_store[head]