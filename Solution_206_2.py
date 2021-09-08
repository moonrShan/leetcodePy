from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution_206:
    def __init__(self):
        self.newHead = ListNode()

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        self.reverseToPrev(None, head)
        return self.newHead

    def reverseToPrev(self, prev: Optional[ListNode], current: Optional[ListNode]) -> Optional[ListNode]:
        if current.next:
            self.reverseToPrev(current, current.next)
        else:
            self.newHead = current
        current.next = prev