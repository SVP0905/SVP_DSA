class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        indegree=[[0]*n for _ in range(m)]

        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(m):
            for j in range(n):
                for dr,dc in directions:
                    nr,nc=dr+i,dc+j
                    if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[i][j]:
                        indegree[nr][nc]+=1
        
        q=deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j]==0:
                    q.append((i,j))
        
        res=0
        while q:
            res+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+r,dc+c
                    if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                        indegree[nr][nc]-=1
                        if indegree[nr][nc]==0:
                            q.append((nr,nc))
        
        
        return res
