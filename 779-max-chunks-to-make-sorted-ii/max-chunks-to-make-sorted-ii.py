class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr=sorted(arr)
        n=len(arr)
        chunks=0
        for i in range(n):
            current_sorted=sorted(arr[0:i+1])
            if current_sorted==sorted_arr[0:i+1]:
                chunks+=1
        return chunks