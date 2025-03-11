# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy 
        #  get left - 1 to know the prev 
        for _ in range(left-1):
            prev = prev.next 

        # i want to be able to reverse from left to rifht 
        curr = prev.next 
        prev_reversed = None 
        for _ in range(right - left + 1):
            temp = curr.next 
            curr.next = prev_reversed 
            prev_reversed = curr 
            curr = temp 
        prev.next.next = curr 
        prev.next = prev_reversed 
        return dummy.next