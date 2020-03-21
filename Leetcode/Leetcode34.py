class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid =  (l+r) // 2
            if nums[mid] == target:
                begin = end = mid
                while begin >= 0 and target == nums[begin]:
                    begin -= 1
                while end < len(nums) and target == nums[end]:
                    end += 1
                return [begin + 1,end - 1]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1,-1]
