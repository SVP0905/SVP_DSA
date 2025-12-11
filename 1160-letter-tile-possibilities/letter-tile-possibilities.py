class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        map_=[0]*26
        for ch in tiles:
            map_[ord(ch)-ord('A')]+=1

        def dfs():
            total=0
            for i in range(26):
                if map_[i]==0:
                    continue
                
                total+=1
                map_[i]-=1
                total+=dfs()
                map_[i]+=1
            
            return total
        
        return dfs()
