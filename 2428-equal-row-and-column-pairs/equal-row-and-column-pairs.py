class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_cnt=Counter(tuple(row) for row in grid)
        cnt=0
        n=len(grid)
        for j in range(n):
            column_tuple=tuple(grid[i][j] for i in range(n))

            if column_tuple in row_cnt:
                cnt+=row_cnt[column_tuple]
        return cnt 