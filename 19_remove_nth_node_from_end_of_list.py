# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # i can make use of a way of two pointers also to get it
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        for i in range(n + 1):
            # this will allow it to get to whats next before it
            first = first.next
        # when thats done with that i move that second loop with the first one
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next