# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # i think it makes sense for me to find the length of the linked list 
        count = 0 
        curr = head 
        while curr:
            count += 1 
            curr = curr.next 
        check = count - n
        if check == 0:
            return head.next
        i = 1 
        curr = head 
        while curr:
            if check == i:
                curr.next = curr.next.next
            i += 1 
            curr = curr.next 
        return head