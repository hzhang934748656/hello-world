class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        res = ['' for _ in range(numRows)]
        row, step = 0, 1
        for i in s:
            res[row] += i
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(res)
        
