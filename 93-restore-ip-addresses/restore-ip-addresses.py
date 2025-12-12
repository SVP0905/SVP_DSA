class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]

        def dfs(start_idx,path):
            if len(path)==4 and start_idx>=len(s):
                res.append('.'.join(path.copy()))
                return
            
            for j in range(start_idx,len(s)):
                cur_sub=s[start_idx:j+1]
                if cur_sub[0]=='0' and len(cur_sub)>1:
                    continue
                if int(cur_sub)>255:
                    continue

                path.append(cur_sub)
                dfs(j+1,path)
                path.pop()
        

        dfs(0,[])
        
        return res