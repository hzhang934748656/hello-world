class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = []
        end_time = []
        for i in range(len(intervals)):
            start_time.append(intervals[i][0])
            end_time.append(intervals[i][1])
        start_time.sort()
        end_time.sort()
        res = 0
        p1 = 0
        p2 = 0
        while p1 < len(start_time):
            if start_time[p1] >= end_time[p2]:
                res -= 1
                p2 += 1
            res += 1
            p1 += 1
        return res
    
            
