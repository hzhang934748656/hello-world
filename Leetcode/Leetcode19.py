# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p2 = p2.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return dummy.next
 #########考虑[1,2]
  ############## 2 的情况，所以先设一个dummy比较好
