class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()  # Sort the array first
        
        # Precompute powers of 2 to avoid repeated calculation
        n = len(nums)
        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i-1] * 2) % MOD
        
        left, right = 0, n - 1
        result = 0
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                # All subsequences starting with nums[left] and ending
                # anywhere from left to right are valid
                # Count = 2^(right-left) because we can choose any subset
                # of elements between left+1 and right (inclusive)
                result = (result + powers[right - left]) % MOD
                left += 1
            else:
                # nums[left] + nums[right] > target
                # Need to reduce the sum, so move right pointer left
                right -= 1
        
        return result