class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(i,sum_,arr):
            if sum_==n and len(arr)==k:
                res.append(arr.copy())
                return
            
            if sum_>n or len(arr)>k or i>9:
                return
            arr.append(i)
            dfs(i+1,sum_+i,arr)

            arr.pop()
            dfs(i+1,sum_,arr)
        
        dfs(1,0,[])
        return res