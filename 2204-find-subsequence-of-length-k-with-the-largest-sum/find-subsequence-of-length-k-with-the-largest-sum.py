class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_vals=[ [nums[i],i] for i in range(len(nums)) ]

        indexed_vals.sort(reverse=True)

        selected_vals=indexed_vals[:k]

        selected_vals.sort(key=lambda x:x[1])

        return [val for val,_ in selected_vals]

