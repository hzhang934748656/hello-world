class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False] * len(nums)
        self.backtracking(sorted(nums),[])
        return self.res
    
    def backtracking(self,nums,temp):
        if len(temp) == len(nums):
            self.res.append(temp[:])
        
        for i in range(len(nums)):
            if self.used[i]: continue
            if i > 0 and nums[i] == nums[i-1] and self.used[i-1]: continue
            self.used[i] = True
            temp.append(nums[i])
            self.backtracking(nums,temp)
            temp.pop()
            self.used[i] = False
