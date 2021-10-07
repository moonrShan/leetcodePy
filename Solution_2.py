# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Solution_206 import ListNode


class Solution_2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        d = sentinel
        total = 0
        while l1 or l2:
            total //= 10
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            d.next = ListNode(total % 10)
            d = d.next

        if total // 10 == 1:
            d.next = ListNode(1)
        return sentinel.next
