class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        val_to_wei={}
        for val,wei in items1:
            val_to_wei[val]=val_to_wei.get(val,0)+wei
        
        for val,wei in items2:
            val_to_wei[val]=val_to_wei.get(val,0)+wei

        res=[[val,wei] for val,wei in val_to_wei.items()]
        res.sort(key=lambda x:x[0])

        return res