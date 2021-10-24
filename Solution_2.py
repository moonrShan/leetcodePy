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


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.graph = collections.defaultdict(list)
        self.children = collections.defaultdict(list)
        for i in range(len(parents)):
            if parents[i] >= 0:
                self.graph[parents[i]].append(i)
        self.dfsCountChildren(0)

        result = 1
        total = len(parents)
        for i in range(len(parents)):
            temp = self.children[i]
            left = temp[0]
            right = temp[1]
            result = max(result, max(left, 1) * max(right, 1) * max(total - left - right - 1, 1)

        return result

    def dfsCountChildren(self, node):
        child = self.graph[node]
        if not child or len(child) == 0:
            self.children[node] = [0, 0]
        if len(child) == 1:
            self.children[node] = [1 + self.dfsCountChildren(child[0]), 0]
        if len(child) == 2:
            self.children[node] = [1 + self.dfsCountChildren(child[0]), 1 + self.dfsCountChildren(child[1])]
        return sum(self.children[node])
