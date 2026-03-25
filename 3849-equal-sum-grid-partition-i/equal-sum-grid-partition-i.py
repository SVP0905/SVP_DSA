class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows=[]
        cols=[]
        
        m,n=len(grid),len(grid[0])

        for i in range(m):
            row_sum=0
            for j in range(n):
                row_sum+=grid[i][j]
            rows.append(row_sum)
        
        for j in range(n):
            cols_sum=0
            for i in range(m):
                cols_sum+=grid[i][j]
            cols.append(cols_sum)
        
        
        total_sum=sum(rows)
        cur_top_sum=0
        for i in range(m-1):
            cur_top_sum+=rows[i]
            
            if cur_top_sum==total_sum-cur_top_sum:
                return True
        

        total_sum=sum(cols)
        cur_left_sum=0
        for j in range(n-1):
            cur_left_sum+=cols[j]
            if cur_left_sum==total_sum-cur_left_sum:
                return True
            
        return False
