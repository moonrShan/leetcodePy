# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Solution_206 import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinal = ListNode(0, head)
        prev = sentinal
        while head and head.next:
            prev.next = self.swap(head, head.next)
            prev = prev.next.next
            head = prev.next
        return sentinal.next

    def swap(self, node1, node2):
        node1.next = node2.next
        node2.next = node1
        return node2