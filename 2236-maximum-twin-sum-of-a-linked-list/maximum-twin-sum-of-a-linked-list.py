# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        cur,prev=slow,None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        first,second=head,prev
        sum_=0
        while second:
            sum_=max(sum_,first.val+second.val)
            first=first.next
            second=second.next
        
        return sum_