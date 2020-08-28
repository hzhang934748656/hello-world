class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = len(nums1)
        y = len(nums2)
        if x > y:
            return self.findMedianSortedArrays(nums2,nums1)
        
        low = 0
        high = x
        while low <= high:
            partitionx = low + (high-low)//2
            partitiony = (x+y+1)//2 - partitionx
            
            left_x = -float('inf') if partitionx==0 else nums1[partitionx-1]
            right_x = float('inf') if partitionx==x else nums1[partitionx]
            
            left_y = -float('inf') if partitiony==0 else nums2[partitiony-1]
            right_y = float('inf') if partitiony==y else nums2[partitiony]
            
            if left_x <= right_y and left_y <= right_x:
                if (x+y)%2==0:
                    return (max(left_x,left_y)+min(right_x,right_y))/2
                else:
                    return max(left_x,left_y)
            elif left_x > right_y:
                high -= 1
            else:
                low += 1
