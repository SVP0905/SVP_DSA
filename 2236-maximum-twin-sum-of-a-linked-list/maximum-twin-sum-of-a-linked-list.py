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
        
        prev,cur=None,slow
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        fs,sc=head,prev
        sum_=0
        while sc:
            sum_=max(sum_,fs.val+sc.val)
            fs=fs.next
            sc=sc.next
        return sum_
