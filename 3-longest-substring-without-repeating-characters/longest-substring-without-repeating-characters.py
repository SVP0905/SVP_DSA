class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        n=len(s)
        for i in range(n):
            hash_=[0]*128
            cur_len=0
            for j in range(i,n):
                if hash_[ord(s[j])]==1:
                    break
                hash_[ord(s[j])]=1
                cur_len+=1
                maxlen=max(maxlen,cur_len)
        return maxlen
