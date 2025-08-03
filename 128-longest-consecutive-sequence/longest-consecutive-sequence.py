class DSU:
    def __init__(self,n):
        self.parent=[0]*(n+1)
        self.size=[1]*(n+1)
        for i in range(n+1):
            self.parent[i]=i
        

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
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
        


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        nums_set=set(nums)
        val_idx={val:i for i,val in enumerate(nums_set)}
        n=len(nums_set)
        dsu=DSU(n)

        for num in nums_set:
            if num+1 in val_idx:
                cur_idx=val_idx[num]
                next_idx=val_idx[num+1]
                dsu.union(cur_idx,next_idx)
        
        return max(dsu.size) if dsu.size else 0

        
        