class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def rec(str_):
            if len(str_)<k:
                return 0
            cnt=Counter(str_)
            for key,val in cnt.items():
                if val<k:
                    pivot=str_.find(key)

                    left=rec(str_[:pivot])
                    right=rec(str_[pivot+1:])

                    return max(left,right)
            
            return len(str_)
        
        return rec(s)