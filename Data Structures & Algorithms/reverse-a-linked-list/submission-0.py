# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stacktop=None

        tail=head
        while tail:
            nxt=tail.next
            tail.next=stacktop
            stacktop=tail
            tail=nxt

        return stacktop
        