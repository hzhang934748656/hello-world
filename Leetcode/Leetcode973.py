class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            if len(heap)<K:
                heapq.heappush(heap,[-(x**2+y**2),(x,y)])
            else:
                heapq.heappushpop(heap,[-(x**2+y**2),(x,y)])
        return [item[1] for item in heap]
        
