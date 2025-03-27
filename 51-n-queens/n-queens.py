class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        res=[]
        leftRow=[0]*n
        leftUpperDiagonal=[0]*(2*n-1)
        leftLowerDiagonal=[0]*(2*n-1)
        self.solve(0,board,res,n,leftRow,leftUpperDiagonal,leftLowerDiagonal)

        return res
    
    def solve(self,col,board,res,n,leftRow,leftUpperDiagonal,leftLowerDiagonal):
        if col==n:
            res.append([''.join(row) for row in board])
            return
        
        for row in range(n):
            if leftRow[row]==0 and leftUpperDiagonal[n-1+col-row]==0 and leftLowerDiagonal[row+col]==0:
                board[row][col]='Q'
                leftRow[row]=1
                leftUpperDiagonal[n-1+col-row]=1
                leftLowerDiagonal[row+col]=1
                self.solve(col+1,board,res,n,leftRow,leftUpperDiagonal,leftLowerDiagonal)
                board[row][col]='.'
                leftRow[row]=0
                leftUpperDiagonal[n-1+col-row]=0
                leftLowerDiagonal[row+col]=0

