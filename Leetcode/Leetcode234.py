# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p1 = p2 =head
        n = 0
        stack = []
        while p2:
            n += 1
            p2 = p2.next
        if n == 1:
            return True
        if n % 2 !=0:
            half = n //2 
            for i in range(half):
                stack.append(p1.val)
                p1 = p1.next
            p1 = p1.next
            while p1:
                temp = stack.pop()
                if p1.val != temp:
                    return False
                p1 = p1.next
            return True
        else:
            half = n //2 
            for i in range(half):
                stack.append(p1.val)
                p1 = p1.next
            while p1:
                temp = stack.pop()
                if p1.val != temp:
                    return False
                p1 = p1.next
            return True
