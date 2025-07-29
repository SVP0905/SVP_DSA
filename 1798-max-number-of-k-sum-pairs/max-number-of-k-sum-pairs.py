class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq=Counter()

        cnt=0
        for n in nums:
            diff=k-n
            if freq[diff]>0:
                cnt+=1
                freq[diff]-=1
            else:
                freq[n]+=1
        return cnt