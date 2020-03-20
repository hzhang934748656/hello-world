class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        dic = {}
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]] + 1
            else:
                res = max(res,i-start+1)
            dic[s[i]] = i
        return res
