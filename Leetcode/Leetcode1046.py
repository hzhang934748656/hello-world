class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        p = len(stones)-1
        if len(stones) == 1:
            return stones[0]
        while p>=1:
            stones.sort()
            if stones[p] == stones[p-1]:
                p -= 2
                if p < 0:
                    return 0
            else:
                stones[p-1] = abs(stones[p] - stones[p-1])
                p -= 1
        return stones[p]
