class DisjointSetUnion:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.parent=[0]*(n+1)
        for i in range(n+1):
            self.parent[i]=i
    
    def findParent(self,node):
        if node==self.parent[node]:
            return node
        else:
            self.parent[node]=self.findParent(self.parent[node])
            return self.parent[node]
    
    def union(self,u,v):
        pu,pv=self.findParent(u),self.findParent(v)

        if pu==pv:
            return False
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pv]<self.rank[pu]:
            self.parent[pv]=pu
        else:
            self.parent[pu]=pv
            self.rank[pv]+=1
        return True


class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        DSU=DisjointSetUnion(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    DSU.union(i,j)
        
        provinces=set()
        for i in range(n):
            provinces.add(DSU.findParent(i))

        return len(provinces)
        

                    
        