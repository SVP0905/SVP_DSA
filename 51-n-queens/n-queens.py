class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        cols=set()
        neg_diag=set() #\ (r-c=constant)
        pos_diag=set() #/ (r+c=constant)

        res=[]
        def dfs(r):
            if r==n:
                copy=[''.join(row) for row in board]
                res.append(copy)
                return
            

            for c in range(n):
                if (c in cols or (r-c) in neg_diag or (r+c) in pos_diag):
                    continue
                
                cols.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                board[r][c]='Q'

                dfs(r+1)

                board[r][c]='.'
                cols.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
        

        dfs(0)

        return res


                
