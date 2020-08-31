class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s,[])
        return self.res
        
        
    def dfs(self,s,temp):
        #base case
        if not s:
            self.res.append(temp[:])
            return
        for i in range(1,len(s)+1):
            if self.isPali(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:],temp)
                temp.pop()
        
    def isPali(self,s):
        return s == s[::-1]
        
