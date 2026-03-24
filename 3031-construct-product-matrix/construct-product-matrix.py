class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD=12345
        n,m=len(grid),len(grid[0])

        # prefix=[[1]*m for _ in range(n)]
        # suffix=[[1]*m for _ in range(n)]

        prod=[[1]*m for _ in range(n)]
        cur_prod=1

        for i in range(n):
            for j in range(m):
                prod[i][j]=cur_prod
                cur_prod=(cur_prod*grid[i][j])%MOD


        cur_prod=1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                prod[i][j]=(prod[i][j]*cur_prod)%MOD
                cur_prod=(cur_prod*grid[i][j])%MOD
        

        # for i in range(n):
        #     for j in range(m):
        #         prod[i][j]=(prefix[i][j]*suffix[i][j])%MOD
        
        return prod
                    
