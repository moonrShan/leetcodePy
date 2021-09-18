import collections
from typing import List


class Solution_1296:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        numsCounter = collections.Counter(nums)
        while numsCounter:
            begin = min(numsCounter.keys())
            for i in range(k):
                if begin + i in numsCounter and numsCounter[begin + i] > 0:
                    numsCounter[begin + i] -= 1
                    if numsCounter[begin + i] == 0:
                        del numsCounter[begin + i]
                else:
                    return False
        return False if numsCounter else True

