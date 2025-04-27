# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # this is just a case of where i know its a single digit so
        # i think if i do a modulus of 10 and i get the remainder then i take the value and remainder
        res = ListNode(0)
        rem = 0
        node = res
        while l1 and l2:
            curr = rem + l1.val + l2.val
            node.next = ListNode((curr % 10))
            rem = curr // 10
            l1 = l1.next
            l2 = l2.next
            node = node.next
        while l1:
            curr = rem + l1.val
            node.next = ListNode((curr % 10))
            rem = curr // 10
            l1 = l1.next
            node = node.next
        while l2:
            curr = rem + l2.val
            node.next = ListNode((curr % 10))
            rem = curr // 10
            l2 = l2.next
            node = node.next
        if rem != 0:
            node.next = ListNode(rem)
        return res.next