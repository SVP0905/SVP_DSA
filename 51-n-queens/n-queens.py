class Solution:
    def isSafe(self,row,col,board,n):
        r,c=row,col
        while r>=0 and c>=0:
            if board[r][c]=='Q':
                return False
            r-=1
            c-=1
        
        r,c=row,col
        while r<n and c>=0:
            if board[r][c]=='Q':
                return False
            r+=1
            c-=1
        
        for c in range(col):
            if board[row][c]=='Q':
                return False
        
        return True
        
        

    def solve(self,col,board,ans,n):
        if col==n:
            ans.append([''.join(row) for row in board])
            return
        
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col]='Q'
                self.solve(col+1,board,ans,n)
                board[row][col]='.'

    
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[['.']*n for _ in range(n)]
        self.solve(0,board,ans,n)
        return ans