import collections


class Solution_3_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        counter = collections.Counter()
        for right in range(len(s)):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            result = max(result,right-left+1)

        return result