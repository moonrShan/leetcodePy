import collections


class Solution_424:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        left = 0
        result = 0
        distinctCount = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] == 1:
                distinctCount += 1
            while distinctCount > 1 and sum(sorted([v for k,v in counter.items()])[:-1]) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    distinctCount -= 1
                left += 1
            result = max(result, right-left + 1)
        return result