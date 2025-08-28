class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        
        for k in range(n):
            row=[]
            for i in range(n):
                for j in range(n):
                    if i-j==k:
                        row.append(grid[i][j])
            
            row.sort(reverse=True)
        
            idx=0
            for i in range(n):
                for j in range(n):
                    if i-j==k:
                        grid[i][j]=row[idx]
                        idx+=1
        

        for k in range(1,n):
            row=[]
            for i in range(n):
                for j in range(n):
                    if j-i==k:
                        row.append(grid[i][j])
            
            row.sort()
            
            idx=0
            for i in range(n):
                for j in range(n):
                    if j-i==k:
                        grid[i][j]=row[idx]
                        idx+=1
        
        return grid
        


        