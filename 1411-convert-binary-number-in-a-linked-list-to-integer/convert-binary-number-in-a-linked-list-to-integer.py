# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur=head
        num=[]
        while cur:
            num.append(cur.val)
            cur=cur.next
        
        i=0
        res=0
        for num in reversed(num):
            res+=num*2**i
            i+=1
        return res