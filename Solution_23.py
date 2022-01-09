# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional
from Solution_206 import ListNode

class Solution_23:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        sentinal = ListNode(0,None)
        result = sentinal
        for i,head in enumerate(lists):
            if head:
                heapq.heappush(heap,[head.val,i,head])
        while heap:
            val,i,node = heapq.heappop(heap)
            result.next = ListNode(val,None)
            result = result.next
            if node.next:
                heapq.heappush(heap,[node.next.val,i,node.next])
        return sentinal.next