class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    
    def find(self,u):
        if u!=self.parent[u]:
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        all_edges=[]




        for i in range(n):
            for j in range(i+1,n):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                all_edges.append((dist,i,j))
        
        all_edges.sort()

        dsu=DSU(n)
        total_cost=0
        edge_cnt=0

        for weight,u,v in all_edges:
            if dsu.union(u,v):
                total_cost+=weight
                edge_cnt+=1

                if edge_cnt==n-1:
                    break
        
        return total_cost

        


        