# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        
        l,r=0,len(arr)-1
        res=0
        while l<=r:
            sum_=0
            sum_=arr[l]+arr[r]
            res=max(res,sum_)
            l+=1
            r-=1
        return res