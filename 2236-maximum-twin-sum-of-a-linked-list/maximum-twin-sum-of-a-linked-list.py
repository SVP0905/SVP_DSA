# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head

        slow,fast=head,head.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        cur=slow.next
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt

        max_=0
        while prev:
            sum_=head.val+prev.val
            max_=max(sum_,max_)
            head=head.next
            prev=prev.next
        return max_