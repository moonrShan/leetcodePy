from typing import List


class Solution_2032:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = set()
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        result |= (set1 & set2)
        result |= (set2 & set3)
        result |= (set1 & set3)

        return list(result)