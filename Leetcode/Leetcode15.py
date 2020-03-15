class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-1] + nums[n-2] < 0:
                continue
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, n-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res
                    
                    
                
