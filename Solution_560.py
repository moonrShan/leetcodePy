class Solution_560:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumDict = collections.defaultdict(int)
        prefixSumDict[0] = 1
        count, prefixSum = 0, 0
        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixSumDict:
                count += prefixSumDict[prefixSum - k]
            prefixSumDict[prefixSum] += 1
        return count