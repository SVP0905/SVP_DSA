class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def isPalindrome(i,j):
            if i>=j:
                return True
            
            if i==j:
                return False
            
            if s[i]==s[j]:
                return isPalindrome(i+1,j-1)
            
            return False
        
        n=len(s)
        res=0
        for i in range(n):
            for j in range(i,n):
                if isPalindrome(i,j):
                    res+=1
        
        return res