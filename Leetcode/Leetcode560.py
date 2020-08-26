class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        dic = {0:1}
        for i in range(len(nums)):
            total += nums[i]
            if total-k in dic:
                count += dic[total-k]
            if total not in dic:
                dic[total] = 1
            else:
                dic[total] += 1
        return count

        
