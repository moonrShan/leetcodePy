# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from Solution_206 import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = 0, 0
        while l1:
            s1 *= 10
            s1 += l1.val
            l1 = l1.next
        while l2:
            s2 *= 10
            s2 += l2.val
            l2 = l2.next

        s3 = s1 + s2
        prev = None
        cur = None
        while s3 > 0:
            cur = ListNode(s3 % 10)
            cur.next = prev
            prev = cur
            s3 = s3 // 10
        return cur if cur else ListNode(0)