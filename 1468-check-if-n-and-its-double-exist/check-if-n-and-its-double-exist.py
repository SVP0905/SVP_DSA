class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        map_={}
        for i in range(len(arr)):
            map_[arr[i]]=i
        
        for i,val in enumerate(arr):
            if 2*val in map_ and i!=map_[val*2]:
                return True
        
        return False