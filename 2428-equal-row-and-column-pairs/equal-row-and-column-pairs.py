class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter=Counter()
        n=len(grid)
        for i in range(n):
            row_tuple=tuple(grid[i])

            counter[row_tuple]+=1
        
        pair=0
        for j in range(n):
            col_tuple=tuple(grid[i][j] for i in range(n))

            pair+=counter[col_tuple]
        
        return pair