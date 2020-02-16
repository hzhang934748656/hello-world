class Solution:
    def removeDuplicates(self,nums):
        
        if not nums:
            return 0;
        lenth = 0
        for i in range(len(nums)):
            if nums[lenth] != nums[i]:
                lenth += 1
                nums[lenth] = nums[i]
        return lenth + 1
        
        
