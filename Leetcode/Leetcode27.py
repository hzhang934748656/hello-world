class Solution:
    def removeElement(self, nums,val):
        front = 0
        rear = len(nums) - 1
        while(front<=rear):
            if nums[front] == val:
                nums[front], nums[rear] = nums[rear], nums[front]
                rear -= 1
            else:
                front += 1
        return rear + 1
    
                
        
