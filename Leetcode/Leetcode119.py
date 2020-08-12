class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] + [0] * rowIndex
        for _ in range(rowIndex):
            for j in range(rowIndex,0,-1):
                res[j] = res[j] + res[j-1]
        return res
        
