class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_alpha=set(s)
        cnt=0
        for a in unique_alpha:
            first=s.find(a)
            last=s.rfind(a)

            if last-first>1:
                middle_stuff=s[first+1:last]
                middle_unique=set(middle_stuff)

                cnt+=len(middle_unique)
        
        return cnt