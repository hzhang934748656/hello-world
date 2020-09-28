class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s,dp,wordDict):
            if s in dp:
                return dp[s]
            if s in wordDict:
                dp[s] = True
                return True
            for i in range(1,len(s)):
                part = s[i:]
                if part in wordDict and helper(s[:i],dp,wordDict):
                    dp[s] = True
                    return True
            dp[s] = False
            return False
        return helper(s,{},set(wordDict))
        
