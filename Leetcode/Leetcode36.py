class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        def check(unit):
            unit = [x for x in unit if x != "."]
            return len(unit) == len(set(unit))
        def check_row():
            for row in board:
                if not check(row):
                    return False
            return True
        def check_col():
            for col in zip(*board):
                if not check(col):
                    return False
            return True
        def check_block():
            for i in [0,3,6]:
                for j in [0,3,6]:
                    block = [board [x][y] for x in range(i,i+3) for y in range(j,j+3)]
                    if not check(block):
                        return False
            return True
        return check_row() and check_col() and check_block()
                
