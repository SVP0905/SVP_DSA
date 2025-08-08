class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        indegree=[[0]*n for _ in range(m)]

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                for dr,dc in directions:
                    new_dr,new_dc=dr+i,dc+j
                    if (0<=new_dr<m and 0<=new_dc<n and matrix[new_dr][new_dc]>matrix[i][j]):
                        indegree[new_dr][new_dc]+=1
        
        q=deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j]==0:
                    q.append((i,j))

        
        LIS=0
        while q:

            for _ in range(len(q)):
                x,y=q.popleft()
                for dr,dc in directions:
                    new_dr,new_dc=dr+x,dc+y
                    if (0<=new_dr<m and 0<=new_dc<n and matrix[new_dr][new_dc]>matrix[x][y]):
                        indegree[new_dr][new_dc]-=1
                        if indegree[new_dr][new_dc]==0:
                            q.append((new_dr,new_dc))
            LIS+=1

        return LIS