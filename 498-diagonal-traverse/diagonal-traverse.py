class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n=len(mat),len(mat[0])

        res=[]
        for k in range(m+n-1):
            diagonal=[]
            for i in range(m):
                j=k-i
                if 0<=j<n:
                    diagonal.append(mat[i][j])
                        

            print(diagonal)

            if k%2==0:
                diagonal.reverse()
            
            for val in diagonal:
                res.append(val)        
        
        return res
