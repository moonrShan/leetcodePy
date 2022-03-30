from typing import List


class Solution_632:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        mergedList = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, [num[0], i, 0])
        while heap:
            val, numIndex, numPos = heapq.heappop(heap)
            mergedList.append([val, numIndex])
            if numPos < len(nums[numIndex]) - 1:
                heapq.heappush(heap, [nums[numIndex][numPos + 1], numIndex, numPos + 1])
        left = 0
        coveredList = collections.defaultdict(int)
        result = [float(-inf), float(inf)]
        for right in range(len(mergedList)):
            coveredList[mergedList[right][1]] = right
            while len(coveredList) == len(nums):
                if mergedList[right][0] - mergedList[left][0] < result[1] - result[0]:
                    result = [mergedList[left][0], mergedList[right][0]]
                if coveredList[mergedList[left][1]] == left:
                    del coveredList[mergedList[left][1]]
                left += 1
        return result
