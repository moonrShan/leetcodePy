import collections
from typing import List


class Solution_239:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result  = []
        queue = collections.deque()
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            while queue and queue[0] <=  i - k:
                queue.popleft()
            result.append(nums[queue[0]])
        return result[k-1:]