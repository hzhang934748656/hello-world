class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def process(S):
            stack = []
            for i in S:
                if i !='#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return process(S) == process(T)
                
