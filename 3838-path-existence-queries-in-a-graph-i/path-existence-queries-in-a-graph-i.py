class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1]*n
    

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
        
        return True

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu=DSU(n)

        for i in range(1,n):
            dist=nums[i]-nums[i-1]
            if dist<=maxDiff:
                dsu.union(i,i-1)

        

        ans=[]
        for u,v in queries:
            pu=dsu.find(u)
            pv=dsu.find(v)
            if pu==pv:
                ans.append(True)
            else:
                ans.append(False)

        return ans