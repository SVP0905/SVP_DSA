class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count=Counter(tiles)
        def backtrack():
            nonlocal total
            nonlocal count
            for c in count:
                if count[c]>0:
                    count[c]-=1
                    total+=1
                    backtrack()
                    count[c]+=1
        total=0
        backtrack()

        return total