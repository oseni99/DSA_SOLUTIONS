# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # very similar to normal reverse a linked list
        # the left anf right is places and its 1 indexed
        # do a normal reversal but use it with a for loop

        # a dummyNode for if left is 1

        dummy = ListNode(0, head)
        curr = dummy

        for _ in range(left - 1):
            curr = curr.next

        prevLeft = curr
        curr = curr.next

        prev = None
        first = curr
        for _ in range(right - left + 1):
            # now reverse
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        prevLeft.next = prev
        first.next = curr

        return dummy.next