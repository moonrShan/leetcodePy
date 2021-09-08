# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution_206:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prevNode = None
        while(head):
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode