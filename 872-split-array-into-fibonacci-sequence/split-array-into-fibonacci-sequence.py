class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res=[]


        def dfs(start_i,path):
            if start_i>=len(num):
                return len(path)>=3
                

            
            for j in range(start_i,len(num)):
                chunk=num[start_i:j+1]
                val=int(chunk)

                # Constraint: Leading zero and Constraint: Size limit
                if (chunk[0]=='0' and len(chunk)>1) or val>2**31-1:
                    break
                
                if len(path)>=2:
                    needed=path[-1]+path[-2]
                    if val<needed:
                        continue
                    if val>needed:
                        break
                
                path.append(val)

                if dfs(j+1,path):
                    return True
                
                path.pop()

            return False
        
        
        if dfs(0,res):
            return res
        else:
            return []

