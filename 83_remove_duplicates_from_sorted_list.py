# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # since i know that its always sorted 
        # i check one of them and i keep going and when i see another thats not it 
        # i point my next pointer to it 
        curr = head 
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  
            else:
                curr = curr.next 
        return head