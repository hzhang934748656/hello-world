class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(nums,temp,i):
            self.ans.append(temp[:])
            for i in range(i,len(nums)):
                temp.append(nums[i])
                dfs(nums,temp,i+1)
                temp.pop()
            
        dfs(nums,[],0)
        return self.ans
