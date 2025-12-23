class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD=10**9+7
        vowels=set('aeiou')

        @cache
        def dfs(i,last_ch):
            if i==n:
                return 1
            
            cnt=0
            for ch in vowels:
                if last_ch==None:
                    cnt=(cnt+dfs(i+1,ch))%MOD
                
                if last_ch=='a' and ch=='e':
                    cnt=(cnt+dfs(i+1,ch))%MOD
                
                if last_ch=='e' and (ch=='a' or ch=='i'):
                    cnt=(cnt+dfs(i+1,ch))%MOD
                
                if last_ch=='i' and ch!='i':
                    cnt=(cnt+dfs(i+1,ch))%MOD
                
                if last_ch=='o' and (ch=='i' or ch=='u'):
                    cnt=(cnt+dfs(i+1,ch))%MOD
                
                if last_ch=='u' and ch=='a':
                    cnt=(cnt+dfs(i+1,ch))%MOD
            return cnt%MOD
        
        return dfs(0,None)%MOD