class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size=2*n-1

        res=[0]*size
        used=[False]*(n+1)

        def dfs(i):
            if i==size:
                return True
            
            if res[i]!=0:
                return dfs(i+1)
            

            for num in range(n,0,-1):
                if used[num]:
                    continue
                

                if num==1:
                    res[i]=1
                    used[1]=True
                    if dfs(i+1): return True

                    res[i]=0
                    used[1]=False
                else:
                    target_i=i+num

                    if target_i<size and res[target_i]==0:
                        res[i]=num
                        res[target_i]=num
                        used[num]=True
                        if dfs(i+1): return True

                        res[i]=0
                        res[target_i]=0
                        used[num]=False
            return False
        

        dfs(0)

        return res
                
                