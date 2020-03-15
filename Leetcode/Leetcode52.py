class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        res = []
        while i < len(intervals):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            if res:
                prev_start = res[-1][0]
                prev_end = res[-1][1]
                if curr_start <= prev_end:
                    res[-1][1] = max(prev_end,curr_end)
                else:
                    res.append([curr_start,curr_end])
                i += 1
            else:
                res.append([curr_start,curr_end])
                i += 1
        return res
                
            
        
