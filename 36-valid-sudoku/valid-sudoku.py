class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        submat=defaultdict(set)

        m,n=len(board),len(board[0])

        for i in range(m):
            for j in range(n):
                val=board[i][j]

                if val=='.':
                    continue
                
                if (val in rows[i] or val in cols[j] or val in submat[(i//3,j//3)]):
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                submat[(i//3,j//3)].add(val)
        
        return True