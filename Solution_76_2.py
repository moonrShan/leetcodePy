import collections

class Solution_76:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        left = 0
        resultLength = float('inf')
        result = ''

        for right in range(len(s)):
            counter[s[right]] -= 1

            while left < right and counter[s[left]] < 0:
                counter[s[left]] += 1
                left += 1

            if all([v <= 0 for k, v in counter.items()]) and right - left + 1 < resultLength:
                resultLength = right - left + 1
                result = s[left: right + 1]

        return result


