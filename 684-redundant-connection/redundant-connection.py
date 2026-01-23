class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    

    def find(self,u):
        if u==self.parent[u]:
            return u
        
        self.parent[u]=self.find(self.parent[u])

        return self.parent[u]
    

    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)
        if pv==pu:
            return False
        
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=(len(edges)+1)
        dsu=DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
    

