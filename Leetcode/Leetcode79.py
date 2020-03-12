class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtracking(board,i,j,word,0):
                    return True
        return False
    def backtracking(self,board,i,j,word,index):
        if index == len(word):
            return True
        if i < 0 or i >=len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        board[i][j] = '#'
        found = self.backtracking(board,i+1,j,word,index+1) or \
                self.backtracking(board,i-1,j,word,index+1) or \
                self.backtracking(board,i,j+1,word,index+1) or \
                self.backtracking(board,i,j-1,word,index+1)
        board[i][j] = word[index]
        return found
        #经典backtraing
