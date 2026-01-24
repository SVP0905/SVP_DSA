class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1]*n
        self.comp=n
    

    def find(self,u):
        if u!=self.parent[u]:
            self.parent[u]=self.find(self.parent[u])
            return self.parent[u]

        return self.parent[u]
    
    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)
        if pu==pv:
            return 
        
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        
        self.comp-=1
        

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        dsu=DSU(n)

        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    dsu.union(i,j)
        
        return n-dsu.comp
