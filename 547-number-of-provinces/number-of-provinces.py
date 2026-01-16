class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
        self.num_comps=n
    

    def find(self,u):
        if u==self.parent[u]:
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
        

        self.num_comps-=1
        return True
    


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        dsu=DSU(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    dsu.union(i,j)
        
        return dsu.num_comps
        



            

        