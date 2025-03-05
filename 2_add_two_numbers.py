# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # create a new listNode to store the sum of those numbers
        # so two pointers to check
        dummy = ListNode(0)
        curr = dummy
        overs = 0
        while l1 and l2:
            res = l1.val + l2.val
            if overs:
                res += overs
            overs = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        # i know that if one is shorter than the other
        while l1:
            res = l1.val
            if overs:
                res += overs
            overs = res // 10
            curr.next = ListNode(res % 10)
            l1 = l1.next
            curr = curr.next
        while l2:
            res = l2.val
            if overs:
                res += overs
            overs = res // 10
            curr.next = ListNode(res % 10)
            l2 = l2.next
            curr = curr.next
        # this will check if theres any overs added left 
        if overs:
            curr.next = ListNode(overs)
        return dummy.next