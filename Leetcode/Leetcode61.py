# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        if n==1 or k==0 or n==0:
            return head
        k = k % n
        if k==0:
            return head
        p1,p2 = head,head
        for i in range(k):
            p2 = p2.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next
        result = p1.next
        p1.next = None
        p2.next = head
        return result
