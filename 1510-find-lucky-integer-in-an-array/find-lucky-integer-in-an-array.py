class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        counter=Counter(arr)

        for key,val in counter.items():
            if key==val:
                return key
        return -1