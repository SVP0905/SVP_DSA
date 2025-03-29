class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        map_=defaultdict(int)
        for i in range(n):
            for j in range(n):
                map_[grid[i][j]]+=1
        
        ans=[]
        for i in range(1,n**2+1):
            if map_[i] and map_[i]==2:
                ans.append(i)
                break

        for i in range(1,n**2+1):
            if not map_[i]:
                ans.append(i)
                break
        return ans