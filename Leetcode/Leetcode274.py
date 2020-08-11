class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        n = len(citations)
        for i in citations:
            if i >= n:
                return n
            n -= 1
        return 0
        
