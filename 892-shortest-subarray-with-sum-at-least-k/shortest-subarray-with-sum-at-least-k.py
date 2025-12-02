class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        
        # 2. Monotonic Deque
        # Stores indices 'i' of the P array
        dq=deque()
        res=float('inf')
        for i in range(n+1):
            # CHECK 1: Try to shrink the window from the left
            # If P[i] - P[first_in_deque] >= k, we found a valid subarray!
            # We record the length and pop from left because extending further right
            # from this start point 'dq[0]' will only make the subarray longer (worse).
            while dq and prefix[i]-prefix[dq[0]]>=k:
                res=min(res,i-dq[0])
                dq.popleft()
            

            # CHECK 2: Maintain Monotonicity (The "Optimization" Step)
            # If the current prefix sum P[i] is smaller than the last one in deque,
            # then P[i] is a strictly better starting point for future subarrays.
            # Why? Because P[i] is smaller (easier to reach >= k diff) AND has a larger index (shorter length).
            # So we remove the useless indices from the back.
            while dq and prefix[i]<prefix[dq[-1]]:
                dq.pop()

            dq.append(i)
        
        return res if res!=float('inf') else -1
            
        
