# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # add a reference to the nodes inside a list
        # use two pointer on it
        # modify the pointers
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        l = 0
        r = len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            if l < r: # this will check if its not the same and l and r dont cross 
                nodes[r].next = nodes[l]
                r -= 1
        # this will ensure that the last node points to None
        nodes[l].next = None