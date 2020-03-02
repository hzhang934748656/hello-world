class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in table:
                stack.append(i)
            elif not stack:
                return False
            elif table[stack.pop()]!=i:
                return False
        if not stack:
            return True
        else:
            return False
