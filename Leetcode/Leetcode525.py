class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lenth = 0
        total = 0
        dic = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                total += 1
            else:
                total -= 1
            if total in dic:
                lenth = max(lenth,i-dic[total])
            else:
                dic[total] = i
            if total == 0:
                lenth = i+1

        return lenth
                
                
        
        
