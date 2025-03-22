class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        map_={}
        for val,wei in items1:
            map_[val]=map_.get(val,0)+wei
        
        for val,wei in items2:
            map_[val]=map_.get(val,0)+wei
        
        res=[[val,wei] for val,wei in map_.items()]

        res.sort(key=lambda x:x[0])

        return res
