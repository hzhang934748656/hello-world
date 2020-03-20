class Solution:
    def get_long_pair(self,s,l,r):
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    def longestPalindrome(self, s: str) -> str:
        res = ''
        
        for i in range(len(s)):
            len1 = self.get_long_pair(s,i,i)
            if len(len1) > len(res):
                res = len1
            len2 = self.get_long_pair(s,i,i+1)
            if len(len2) > len(res):
                res = len2
        return res
        
