class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dnc(str_):
            if len(str_)<k:
                return 0
            
            cnt=Counter(str_)
            for key,val in cnt.items():
                if val<k:
                    pivot=str_.find(key)

                    return max(dnc(str_[:pivot]),dnc(str_[pivot+1:]))
            
            return len(str_)
        
        return dnc(s)