class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD=12345
        n,m=len(grid),len(grid[0])

        prefix=[[1]*m for _ in range(n)]
        suffix=[[1]*m for _ in range(n)]

        cur_prefix=1
        for i in range(n):
            for j in range(m):
                prefix[i][j]=cur_prefix
                cur_prefix=(cur_prefix*grid[i][j])%MOD


        cur_suffix=1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                suffix[i][j]=cur_suffix
                cur_suffix=(cur_suffix*grid[i][j])%MOD
        

        prod=[[1]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                prod[i][j]=(prefix[i][j]*suffix[i][j])%MOD
        
        return prod
                    
