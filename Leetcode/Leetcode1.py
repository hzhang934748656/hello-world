class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if target-nums[i] == nums[j]:
                    return [i,j]
                    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(0,len(nums)):
            if target - nums[i] not in hash_table:
                hash_table[nums[i]] = i
            else:
                return ([hash_table[target-nums[i]],i])
