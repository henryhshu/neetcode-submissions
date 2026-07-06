# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse through the entire linked list
        # get the length - n value
        sz = 0
        curr = head
        while curr:
            curr = curr.next
            sz += 1
        n = sz - n
        if n == 0:
            return head.next
        curr = head
        for _ in range(n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
        
