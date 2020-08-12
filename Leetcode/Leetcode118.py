class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        row = []
        for i in range(numRows):
            row = [1] + [0] * i
            row[-1] = 1
            for j in range(i-1,0,-1):
                row[j] = res[i-1][j] + res[i-1][j-1]
            res.append(row)
        return res
