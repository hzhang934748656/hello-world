# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
    
        #第一个循环找出是否存在循环链表，用fast和slow双指针，第二个循环来找到循环开始点
