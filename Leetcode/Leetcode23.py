# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2(l1,l2):
            head = curr = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return head.next
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists)//2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return merge2(left,right)
                
        
