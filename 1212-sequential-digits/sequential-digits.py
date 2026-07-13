class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def dfs(val,last_digit):
            if val>high:
                return 
            
            if low<=val<=high:
                res.append(val)
            
            if last_digit<9:
                next_digit=last_digit+1
                val=(val*10)+next_digit
                dfs(val,next_digit)
            

        res=[]
        for i in range(1,10):
            dfs(i,i)
        
        return sorted(res)
            