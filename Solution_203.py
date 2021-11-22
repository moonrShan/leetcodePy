# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Solution_206 import ListNode


class Solution_203:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinal = ListNode(0,head)
        prev = sentinal
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return sentinal.next