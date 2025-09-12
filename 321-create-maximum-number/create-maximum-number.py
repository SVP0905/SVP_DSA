class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m,n=len(nums1),len(nums2)

        def most_subs(arr,k):
            n1=len(arr)
            stack=[]
            for i in range(n1):
                while (stack and arr[i]>stack[-1] and len(stack)+(n1-i)>k):
                    stack.pop()
                
                if len(stack)<k:
                    stack.append(arr[i])
            
            return stack


        def merge(arr1,arr2):
            m1,n1=len(arr1),len(arr2)
            i,j=0,0
            res=[]
            while i<m1 and j<n1:
                if arr1[i:]>arr2[j:]:
                    res.append(arr1[i])
                    i+=1
                else:
                    res.append(arr2[j])
                    j+=1
            
            return res+arr1[i:]+arr2[j:]
        

        best=[]
        for i in range(max(0,k-n),min(k,m)+1):
            sub1=most_subs(nums1,i)
            sub2=most_subs(nums2,k-i)
            candidate=merge(sub1,sub2)
            if candidate>best:
                best=candidate
        
        return best