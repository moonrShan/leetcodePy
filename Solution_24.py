# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution_24:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head and head.next:
            self.swap(prev, head, head.next)
            prev = head
            head = head.next
        return dummy.next

    def swap(self, prev, head, headNext):
        prev.next = headNext
        head.next = headNext.next
        headNext.next = head
