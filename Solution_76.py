import collections
class Solution_76:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        left, right = 0, -1
        resultLength = float('inf')
        result = ''

        while right < len(s):
            while any([v > 0 for k, v in counter.items()]):
                right += 1
                if right == len(s):
                    return result
                counter[s[right]] -= 1

            while counter[s[left]] < 0:
                counter[s[left]] += 1
                left += 1

            if right - left + 1 < resultLength:
                resultLength = right - left + 1
                result = s[left: right + 1]

            counter[s[left]] += 1
            left += 1

        return result









