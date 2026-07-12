class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=len(arr)
        # sorted_unique_elements=sorted(set(arr))


        unique=set(arr)
        unique_arr=[num for num in unique]
        unique_arr.sort()
        
        map_={}
        for i in range(1,len(unique_arr)+1):
            map_[unique_arr[i-1]]=i
        
        ans=[]
        for i in range(n):
            ans.append(map_[arr[i]])
        
        return ans

        

        
        

        