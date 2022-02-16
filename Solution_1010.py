import collections
from typing import List


class Solution_1010:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        waitDict = collections.defaultdict(int)
        result = 0
        for t in time:
            result += waitDict[t % 60]
            waitDict[60 - t % 60] += 1
        return result + waitDict[60] * (waitDict[60] - 1) // 2