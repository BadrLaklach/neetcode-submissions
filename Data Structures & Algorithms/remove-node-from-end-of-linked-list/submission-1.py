# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current=head
        lenList=0
        while current:
            lenList+=1
            current=current.next
        
        if n==lenList:
            return head.next
        
        if n==1:
            current=head
            while current:
                if not current.next.next:
                    current.next=None
                current=current.next
            return head

        current=head

        stack=None
        while current:
            temp=current.next
            current.next=stack
            stack=current
            current=temp

        current=stack
        i=2
        while current:
            if i==n:
                current.next=current.next.next
            i+=1
            current=current.next
        
        current=stack
        stack=None
        while current:
            temp=current.next
            current.next=stack
            stack=current
            current=temp
        
        return stack












        