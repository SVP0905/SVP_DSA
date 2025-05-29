class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter=Counter()

        for i in range(len(grid)):
            row_tuple=tuple(grid[i])
            counter[row_tuple]+=1
        
        pair=0

        for j in range(len(grid)):
            col_tuple=tuple(grid[i][j] for i in range(len(grid)))

            pair+=counter[col_tuple]
        
        return pair