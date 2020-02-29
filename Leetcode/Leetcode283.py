class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        last = 0
        for i in range(n):
            if nums[i] != 0:
                nums[last] = nums[i]
                last += 1
        for i in range(last,n):
            nums[i] = 0
        return nums
