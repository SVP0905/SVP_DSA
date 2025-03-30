class DisjointSetUnion:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.parent=[0]*(n+1)
        for i in range(n+1):
            self.parent[i]=i
        
    def find(self,u):
        if u==self.parent[u]:
            return u
        else:
            self.parent[u]=self.find(self.parent[u])
            return self.parent[u]
    
    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)
        if pu==pv:
            return
        elif self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pv]<self.rank[pu]:
            self.parent[pv]=pu
        else:
            self.parent[pu]=pv
            self.rank[pv]+=1
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        DSU=DisjointSetUnion(n)

        for u,v in connections:
            DSU.union(u,v)
        
        components=set()
        for i in range(n):
            components.add(DSU.find(i))

        return len(components)-1