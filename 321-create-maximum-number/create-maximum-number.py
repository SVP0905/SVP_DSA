class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_seq(seq,length):
            x=len(seq)
            stack=[]
            map_={num:i for i,num in enumerate(seq)}
            for i,num in enumerate(seq):
                while stack and num>stack[-1] and len(stack)-1+(x-i)>=length:
                    stack.pop()
                
                if len(stack)<length:
                    stack.append(num)
            
            return stack
        

        def merge(seq1,seq2):
            res=[]
            while seq1 or seq2:
                if seq1>seq2:
                    res.append(seq1.pop(0))
                else:
                    res.append(seq2.pop(0))
            
            return res

        m,n=len(nums1),len(nums2)
        min_=max(0,k-n)
        max_=min(m,k)
        ans=[]
        for i in range(min_,max_+1):
            seq1=max_seq(nums1,i)
            seq2=max_seq(nums2,k-i)

            cur_res=merge(seq1,seq2)
            if cur_res>ans:
                ans=cur_res
        
        return ans



