class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,l=len(s1),len(s2),len(s3)

        if m+n!=l:
            return False
        

        @cache
        def dfs(i,j):
            k=i+j
            if k==l:
                return True
            
            if i==m:
                if s2[j:]==s3[k:]:
                    return True
                else:
                    return False
            
            if j==n:
                if s1[i:]==s3[k:]:
                    return True
                else:
                    return False
            
            res=False
            if s1[i]==s3[k] and s2[j]==s3[k]:
                res=dfs(i+1,j) or dfs(i,j+1)
                if res:
                    return True
            elif s1[i]==s3[k]:
                res=dfs(i+1,j)
                if res:
                    return True
            elif s2[j]==s3[k]:
                res=dfs(i,j+1)
                if res:
                    return True
            
            return res
        
        return dfs(0,0)