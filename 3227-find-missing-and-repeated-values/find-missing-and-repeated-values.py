class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        map_={}
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in map_:
                    map_[grid[i][j]]=1
                else:
                    map_[grid[i][j]]+=1
        
        res=[]
        for i in range(1,n**2+1):
            if i in map_ and map_[i]==2:
                res.append(i)
                break
        
        for i in range(1,n**2+1):
            if i not in map_:
                res.append(i)
                break

        return res
        
        
