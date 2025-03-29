class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        map_=defaultdict(int)
        for i in range(n):
            for j in range(n):
                map_[grid[i][j]]+=1
        
        res=[]
        for i in range(1,n**2+1):
            if map_[i] and map_[i]==2:
                res.append(i)
                break
        
        for i in range(1,n**2+1):
            if map_[i]==0:
                res.append(i)
                break
        return res