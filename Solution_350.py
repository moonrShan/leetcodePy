import collections
from typing import List


class Solution_350:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = collections.Counter(nums1)
        result = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                result.append(num)
                counter[num] -= 1
        return result