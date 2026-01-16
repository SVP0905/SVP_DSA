class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)

    
    def find(self,u):
        if self.parent[u]==u:
            return u
        
        self.parent[u]=self.find(self.parent[u])

        return self.parent[u]
    

    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)

        if pu==pv:
            return False
        
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        dsu=DSU(m*n)

        directions=[(0,1),(1,0),(0,-1),(-1,0)]


        islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    islands+=1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    idx1=(i*n)+j
                    for dr,dc in directions:
                        new_dr,new_dc=dr+i,dc+j
                        if 0<=new_dr<m and 0<=new_dc<n and grid[new_dr][new_dc]=='1':
                            idx2=(new_dr*n)+new_dc
                            if dsu.union(idx1,idx2):
                                islands-=1
        
        return islands
        