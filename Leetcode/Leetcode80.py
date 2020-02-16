class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        count = 2
        i = 2
        while i < len(nums):
            if nums[count-2] != nums[i]:
                nums[count] = nums[i]
                count += 1
            i += 1
        return count
