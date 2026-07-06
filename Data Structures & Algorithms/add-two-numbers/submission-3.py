# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse the linked list
        # have a carry variable
        carry = 0
        cur = ListNode()
        dummy = cur
        while l1 and l2:
            value = (l1.val + l2.val) % 10
            cur.next = ListNode(value + carry)
            carry = (l1.val + l2.val) // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            cur = cur.next
            l1 = l1.next
        while l2:
            cur.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(carry)
        return dummy.next
            
