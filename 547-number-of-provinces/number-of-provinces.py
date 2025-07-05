class DSU:
    def __init__(self,n):
        self.parent=[0]*(n+1)
        self.rank=[0]*(n+1)
        for i in range(n+1):
            self.parent[i]=i
    
    def find(self,u):
        if u==self.parent[u]:
            return u
        return self.find(self.parent[u])
    

    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)

        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pv]<self.rank[pu]:
            self.parent[pv]=pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
    


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        dsu=DSU(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    dsu.union(i,j)
        
        res=set()
        for i in range(n):
            res.add(dsu.find(i))
        return len(res)