class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        for spell in spells:
            min_potion=math.ceil(success/spell)

            idx=bisect.bisect_left(potions,min_potion)
            cnt=len(potions)-idx
            res.append(cnt)
        return res