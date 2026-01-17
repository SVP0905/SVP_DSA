class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        grid=board
        q=deque()
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and grid[i][j]=='O':
                    grid[i][j]='T'
                    q.append((i,j))
        

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            r,c=q.popleft()

            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='O':
                    grid[nr][nc]="T"
                    q.append((nr,nc))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='O':
                    grid[i][j]='X'
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='T':
                    grid[i][j]='O'
        
                
                
                