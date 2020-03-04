# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val + l2.val+carry) //10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+carry)%10)
                carry = (l2.val + carry)//10
                l2 = l2.next
                p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+carry)%10)
                carry = (l1.val + carry)//10
                l1 = l1.next
                p = p.next
        if carry == 1:
            p.next = ListNode(1)
        return dummy.next
        
