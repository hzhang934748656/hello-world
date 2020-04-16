class Solution:
    def checkValidString(self, s: str) -> bool:
        min_pair = 0
        max_pair = 0
        for i in s:
            if i =='(':
                min_pair += 1
                max_pair += 1
            elif i ==')':
                max_pair -= 1
                min_pair -= 1
            else:
                max_pair += 1
                min_pair -= 1
            if max_pair < 0:
                return False
            if min_pair < 0:
                min_pair = 0
        return min_pair == 0
            
        
