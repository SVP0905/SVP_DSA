class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD=10**9+7
        vowels=set('aeiou')
        transitions={
            'a':['e'],
            'e':['a','i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a']
        }
        
        @cache
        def dfs(i,last_ch):
            if i==n:
                return 1
            
            cnt=0
            for ch in transitions[last_ch]:
                cnt=(cnt+dfs(i+1,ch))%MOD
            
            return cnt
        

        res=0
        for ch in vowels:
            res=(res+dfs(1,ch))%MOD
        
        return res