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
        # the optimal way is to find the middle 
        # reverse that middle which is the 2nd part 
        # after that then swap it and change pointers 
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # at here slow is the middle 
        #reverse it 
        prev = None 
        curr = slow.next
        slow.next = None # this disconnects the first half to the second half 
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 

        # once thats done i just have to swap the pointers 
        first = head 
        second = prev 
        while second:
            temp1 = first.next 
            temp2 = second.next 
            first.next = second 
            second.next = temp1
            first,second =  temp1, temp2