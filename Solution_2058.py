# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Solution_206 import ListNode


class Solution_2058:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticalIndex = []
        i = 0;
        previousValue = 0;
        while head and head.next:
            if previousValue > 0 and head.val > previousValue and head.val > head.next.val:
                criticalIndex.append(i)
            elif previousValue > 0 and head.val < previousValue and head.val < head.next.val:
                criticalIndex.append(i)
            previousValue = head.val
            head = head.next
            i += 1
        if len(criticalIndex) < 2:
            return [-1, -1]

        minDistance = float('inf')
        for i in range(len(criticalIndex) - 1):
            minDistance = min(criticalIndex[i + 1] - criticalIndex[i], minDistance)
        return [minDistance, criticalIndex[-1] - criticalIndex[0]]