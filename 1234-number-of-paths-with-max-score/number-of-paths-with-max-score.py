class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD=10**9+7

        @lru_cache(None)
        def dfs(i,j):
            if not (0<=i<m and 0<=j<n) or board[i][j]=='X':
                return (float('-inf'),0)

            if i==0 and j==0:
                return (0,1)
            
            maxSum=0
            paths=0
            max_left_sum,path_left=dfs(i-1,j)
            max_dia_sum,path_dia=dfs(i-1,j-1)
            max_top_sum,path_top=dfs(i,j-1)

            maxSum=max(max_left_sum,max_dia_sum,max_top_sum)

            if max_left_sum==maxSum:
                paths+=path_left
            
            if max_dia_sum==maxSum:
                paths+=path_dia
            
            if max_top_sum==maxSum:
                paths+=path_top

            
            if board[i][j]=='S':
                return (maxSum+0,paths%MOD)
            else:
                return (maxSum+int(board[i][j]),paths%MOD)

        m,n=len(board),len(board[0])

        res=dfs(m-1,n-1)

        if res[0]==float('-inf'):
            return [0,0]
        else:
            return [res[0],res[1]]
