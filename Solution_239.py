import collections


class Solution_239:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx = collections.deque([0])
        # ans = nums[0]
        result = [nums[0]]
        for i in range(1,len(nums)):
            while mx and nums[mx[-1]]<nums[i]:
                mx.pop()
            mx.append(i)
            while mx and abs(mx[0]-i)>=k:
                mx.popleft()
            # ans = max(ans,nums[mx[0]])
            result.append(nums[mx[0]])
        return result[k-1:]